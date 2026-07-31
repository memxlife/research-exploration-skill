#!/usr/bin/env python3
"""Inventory and structurally check math in Markdown research documents.

This is a source checker. It does not render a document and must never be used
as evidence that equations display correctly in a target viewer.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


INLINE_STYLES = {"dollar", "parenthesis"}
DISPLAY_STYLES = {
    "bracket",
    "bracket-inline",
    "double-dollar",
    "double-dollar-inline",
    "fenced-latex",
    "fenced-math",
    "fenced-tex",
}
MATH_FENCE_LABELS = {
    "latex": "fenced-latex",
    "math": "fenced-math",
    "tex": "fenced-tex",
}
RAW_TEX_COMMAND = re.compile(r"\\[A-Za-z]+")
INLINE_CODE = re.compile(r"(`+)(.*?)(?<!`)\1")
INLINE_DISPLAY_DOLLAR = re.compile(
    r"(?<!\\)\$\$(?=\S)(.+?)(?<!\s)(?<!\\)\$\$"
)
INLINE_DISPLAY_BRACKET = re.compile(r"\\\[(?=\S)(.+?)(?<!\s)\\\]")
INLINE_DOLLAR = re.compile(
    r"(?<!\\)(?<!\$)\$(?!\$)(?=\S)(.+?)(?<!\s)(?<!\\)(?<!\$)\$(?!\$)"
)
INLINE_PAREN = re.compile(r"\\\((.+?)\\\)")
UNESCAPED_DOLLAR = re.compile(r"(?<!\\)\$")


@dataclass
class Inventory:
    inline: dict[str, int] = field(
        default_factory=lambda: {style: 0 for style in sorted(INLINE_STYLES)}
    )
    display: dict[str, int] = field(
        default_factory=lambda: {style: 0 for style in sorted(DISPLAY_STYLES)}
    )

    @property
    def inline_total(self) -> int:
        return sum(self.inline.values())

    @property
    def display_total(self) -> int:
        return sum(self.display.values())


@dataclass(frozen=True)
class ViewerProfile:
    viewer: str
    verified_on: str
    evidence: str
    inline_containers: frozenset[str]
    display_containers: frozenset[str]


def load_profile(path: Path) -> ViewerProfile:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = {
        "viewer",
        "verified_on",
        "evidence",
        "inline_containers",
        "display_containers",
    }
    missing = sorted(required - data.keys())
    if missing:
        raise ValueError(f"missing profile field(s): {', '.join(missing)}")

    inline = frozenset(data["inline_containers"])
    display = frozenset(data["display_containers"])
    unknown_inline = sorted(inline - INLINE_STYLES)
    unknown_display = sorted(display - DISPLAY_STYLES)
    if unknown_inline or unknown_display:
        details = []
        if unknown_inline:
            details.append(f"unknown inline style(s): {', '.join(unknown_inline)}")
        if unknown_display:
            details.append(
                f"unknown display style(s): {', '.join(unknown_display)}"
            )
        raise ValueError("; ".join(details))
    if not inline or not display:
        raise ValueError("profile must permit at least one inline and display style")

    for key in ("viewer", "verified_on", "evidence"):
        if not isinstance(data[key], str) or not data[key].strip():
            raise ValueError(f"profile field {key!r} must be a non-empty string")

    return ViewerProfile(
        viewer=data["viewer"].strip(),
        verified_on=data["verified_on"].strip(),
        evidence=data["evidence"].strip(),
        inline_containers=inline,
        display_containers=display,
    )


def blank_span(text: str, start: int, end: int) -> str:
    return text[:start] + (" " * (end - start)) + text[end:]


def remove_inline_code(line: str) -> str:
    while True:
        match = INLINE_CODE.search(line)
        if match is None:
            return line
        line = blank_span(line, match.start(), match.end())


def consume_inline_math(
    line: str,
    path: Path,
    line_number: int,
    inventory: Inventory,
    errors: list[str],
) -> str:
    for style, pattern in (
        ("parenthesis", INLINE_PAREN),
        ("dollar", INLINE_DOLLAR),
    ):
        while True:
            match = pattern.search(line)
            if match is None:
                break
            if not match.group(1).strip():
                errors.append(
                    f"{path}:{line_number}: empty inline {style} math expression"
                )
            inventory.inline[style] += 1
            line = blank_span(line, match.start(), match.end())
    return line


def consume_inline_display_math(
    line: str,
    path: Path,
    line_number: int,
    inventory: Inventory,
    errors: list[str],
) -> str:
    for style, pattern in (
        ("bracket-inline", INLINE_DISPLAY_BRACKET),
        ("double-dollar-inline", INLINE_DISPLAY_DOLLAR),
    ):
        while True:
            match = pattern.search(line)
            if match is None:
                break
            if not match.group(1).strip():
                errors.append(
                    f"{path}:{line_number}: empty {style} display expression"
                )
            inventory.display[style] += 1
            line = blank_span(line, match.start(), match.end())
    return line


def check_file(
    path: Path, profile: ViewerProfile | None
) -> tuple[list[str], Inventory]:
    errors: list[str] = []
    inventory = Inventory()
    lines = path.read_text(encoding="utf-8").splitlines()

    in_fence = False
    fence_marker = ""
    fence_math_style: str | None = None
    fence_open_line: int | None = None
    fence_has_content = False
    display_style: str | None = None
    display_open_line: int | None = None
    display_has_content = False

    for line_number, original_line in enumerate(lines, start=1):
        stripped = original_line.strip()
        fence_match = re.match(r"^(`{3,}|~{3,})(.*)$", stripped)

        if fence_match:
            marker = fence_match.group(1)
            info_text = fence_match.group(2).strip()
            info = info_text.lower().split(maxsplit=1)
            if not in_fence:
                in_fence = True
                fence_marker = marker
                fence_open_line = line_number
                fence_math_style = (
                    MATH_FENCE_LABELS.get(info[0]) if info else None
                )
                fence_has_content = False
            elif (
                marker[0] == fence_marker[0]
                and len(marker) >= len(fence_marker)
                and not info_text
            ):
                if fence_math_style is not None:
                    if not fence_has_content:
                        errors.append(
                            f"{path}:{fence_open_line}: empty "
                            f"{fence_math_style} display expression"
                        )
                    inventory.display[fence_math_style] += 1
                in_fence = False
                fence_marker = ""
                fence_math_style = None
                fence_open_line = None
                fence_has_content = False
            elif fence_math_style is not None:
                fence_has_content = fence_has_content or bool(stripped)
            continue

        if in_fence:
            if fence_math_style is not None:
                fence_has_content = fence_has_content or bool(stripped)
            continue

        if display_style is not None:
            expected_close = "$$" if display_style == "double-dollar" else r"\]"
            if stripped == expected_close:
                if not display_has_content:
                    errors.append(
                        f"{path}:{display_open_line}: empty {display_style} "
                        "display expression"
                    )
                inventory.display[display_style] += 1
                display_style = None
                display_open_line = None
                display_has_content = False
            else:
                display_has_content = display_has_content or bool(stripped)
            continue

        visible = remove_inline_code(original_line)
        visible_stripped = visible.strip()

        if visible_stripped in {"$$", r"\["}:
            display_style = (
                "double-dollar" if visible_stripped == "$$" else "bracket"
            )
            display_open_line = line_number
            continue

        visible = consume_inline_display_math(
            visible, path, line_number, inventory, errors
        )

        if "$$" in visible:
            errors.append(
                f"{path}:{line_number}: unbalanced or ambiguous display $$ "
                "delimiter"
            )
        if r"\[" in visible or r"\]" in visible:
            errors.append(
                f"{path}:{line_number}: unbalanced or ambiguous display "
                "bracket delimiter"
            )

        visible = consume_inline_math(
            visible, path, line_number, inventory, errors
        )

        if r"\(" in visible or r"\)" in visible:
            errors.append(
                f"{path}:{line_number}: unbalanced inline parenthesis delimiter"
            )

        leftovers = UNESCAPED_DOLLAR.findall(visible)
        if leftovers:
            without_currency = re.sub(r"(?<!\\)\$(?=\d)", "", visible)
            if UNESCAPED_DOLLAR.search(without_currency):
                errors.append(
                    f"{path}:{line_number}: unbalanced or ambiguous inline $ "
                    "delimiter"
                )

        if RAW_TEX_COMMAND.search(visible):
            command = RAW_TEX_COMMAND.search(visible)
            assert command is not None
            errors.append(
                f"{path}:{line_number}: probable raw TeX command "
                f"{command.group(0)!r} outside recognized math"
            )

    if in_fence:
        errors.append(f"{path}: unclosed Markdown fence")
    if display_style is not None:
        close = "$$" if display_style == "double-dollar" else r"\]"
        errors.append(
            f"{path}:{display_open_line}: unclosed {display_style} display; "
            f"expected {close}"
        )

    if profile is not None:
        used_inline = {key for key, count in inventory.inline.items() if count}
        used_display = {
            key for key, count in inventory.display.items() if count
        }
        disallowed_inline = sorted(used_inline - profile.inline_containers)
        disallowed_display = sorted(used_display - profile.display_containers)
        if disallowed_inline:
            errors.append(
                f"{path}: inline container(s) not permitted by viewer profile: "
                f"{', '.join(disallowed_inline)}"
            )
        if disallowed_display:
            errors.append(
                f"{path}: display container(s) not permitted by viewer profile: "
                f"{', '.join(disallowed_display)}"
            )

    return errors, inventory


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Inventory and structurally check Markdown math source. "
            "This command does not render equations."
        )
    )
    parser.add_argument(
        "--profile-file",
        type=Path,
        help=(
            "JSON viewer profile created only after successful inline and "
            "display probes in the exact target viewer"
        ),
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()

    profile: ViewerProfile | None = None
    if args.profile_file is not None:
        try:
            profile = load_profile(args.profile_file)
        except (OSError, ValueError, TypeError, json.JSONDecodeError) as error:
            print(
                f"{args.profile_file}: invalid viewer profile: {error}",
                file=sys.stderr,
            )
            return 2

    all_errors: list[str] = []
    inventories: list[tuple[Path, Inventory]] = []
    for path in args.files:
        if not path.is_file():
            all_errors.append(f"{path}: not a file")
            continue
        errors, inventory = check_file(path, profile)
        all_errors.extend(errors)
        inventories.append((path, inventory))

    for path, inventory in inventories:
        inline_detail = ", ".join(
            f"{style}={count}" for style, count in inventory.inline.items()
        )
        display_detail = ", ".join(
            f"{style}={count}" for style, count in inventory.display.items()
        )
        print(
            f"{path}: inline={inventory.inline_total} ({inline_detail}); "
            f"display={inventory.display_total} ({display_detail})"
        )

    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        print("SOURCE FAIL — rendering not checked.", file=sys.stderr)
        return 1

    if profile is not None:
        print(
            f"Viewer profile: {profile.viewer} "
            f"(verified {profile.verified_on}; evidence: {profile.evidence})"
        )
    print("SOURCE PASS — rendering not checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
