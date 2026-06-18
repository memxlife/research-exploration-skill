#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  ensure_static_viewer_server.sh --root PROJECT_ROOT --port PORT --label LAUNCHD_LABEL [--python PYTHON]

Creates or refreshes a macOS LaunchAgent that serves PROJECT_ROOT through:
  python -m http.server PORT --bind 127.0.0.1 --directory PROJECT_ROOT

This is for static research viewers that should stay available across Codex
turns and browser reloads.
USAGE
}

ROOT=""
PORT=""
LABEL=""
PYTHON_BIN="${PYTHON:-$(command -v python3)}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      ROOT="${2:-}"
      shift 2
      ;;
    --port)
      PORT="${2:-}"
      shift 2
      ;;
    --label)
      LABEL="${2:-}"
      shift 2
      ;;
    --python)
      PYTHON_BIN="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ -z "$ROOT" || -z "$PORT" || -z "$LABEL" || -z "$PYTHON_BIN" ]]; then
  usage >&2
  exit 2
fi

if [[ ! -d "$ROOT" ]]; then
  echo "Project root does not exist: $ROOT" >&2
  exit 1
fi

case "$PORT" in
  ''|*[!0-9]*)
    echo "Port must be an integer: $PORT" >&2
    exit 1
    ;;
esac

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "Python executable is not runnable: $PYTHON_BIN" >&2
  exit 1
fi

PLIST="$HOME/Library/LaunchAgents/${LABEL}.plist"
OUT_LOG="/tmp/${LABEL}.out.log"
ERR_LOG="/tmp/${LABEL}.err.log"
USER_ID="$(id -u)"

mkdir -p "$HOME/Library/LaunchAgents"

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${PYTHON_BIN}</string>
    <string>-m</string>
    <string>http.server</string>
    <string>${PORT}</string>
    <string>--bind</string>
    <string>127.0.0.1</string>
    <string>--directory</string>
    <string>${ROOT}</string>
  </array>
  <key>WorkingDirectory</key>
  <string>${ROOT}</string>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>StandardOutPath</key>
  <string>${OUT_LOG}</string>
  <key>StandardErrorPath</key>
  <string>${ERR_LOG}</string>
</dict>
</plist>
EOF

launchctl bootout "gui/${USER_ID}" "$PLIST" >/dev/null 2>&1 || true
launchctl bootstrap "gui/${USER_ID}" "$PLIST"
launchctl enable "gui/${USER_ID}/${LABEL}"

URL="http://127.0.0.1:${PORT}/"
for _ in 1 2 3 4 5; do
  if curl -fsS -I --max-time 3 "$URL" >/dev/null; then
    echo "Static viewer server is running."
    echo "URL: $URL"
    echo "Project root: $ROOT"
    echo "LaunchAgent: $PLIST"
    echo "Check: launchctl print gui/\$(id -u)/${LABEL}"
    echo "Restart: launchctl kickstart -k gui/\$(id -u)/${LABEL}"
    exit 0
  fi
  sleep 1
done

echo "Server did not return HTTP 200 from $URL" >&2
echo "Check stderr log: $ERR_LOG" >&2
exit 1
