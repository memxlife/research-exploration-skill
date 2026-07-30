#!/usr/bin/env bash
set -euo pipefail

if [[ $# -gt 1 ]]; then
  echo "usage: build_iclr_paper.sh [paper-directory]" >&2
  exit 2
fi

paper_dir="${1:-paper}"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
skill_dir="$(cd "$script_dir/.." && pwd)"
compiler="$skill_dir/tools/tectonic"

if [[ ! -x "$compiler" ]]; then
  compiler="$(command -v tectonic || true)"
fi

if [[ -z "$compiler" ]]; then
  echo "missing Tectonic compiler: place it at $skill_dir/tools/tectonic or add tectonic to PATH" >&2
  exit 1
fi

if [[ ! -f "$paper_dir/main.tex" ]]; then
  echo "missing paper source: $paper_dir/main.tex" >&2
  exit 1
fi

cd "$paper_dir"
"$compiler" main.tex --keep-logs --keep-intermediates
