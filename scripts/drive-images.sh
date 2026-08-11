#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
remote="${X_IMAGE_REMOTE:-personal-drive:X/asset-prompts}"
filter_file="$repo_root/scripts/rclone-images.filter"
transfers="${RCLONE_TRANSFERS:-8}"

if ! command -v rclone >/dev/null 2>&1; then
  echo "Error: rclone is not installed." >&2
  exit 1
fi

usage() {
  cat <<'EOF'
Usage: scripts/drive-images.sh COMMAND

Commands:
  upload       Copy local images to Google Drive without deleting either side
  download     Restore images from Google Drive without deleting either side
  check        Compare local images against Google Drive using hashes
  size-local   Show local image count and total size
  size-remote  Show Google Drive image count and total size

Environment:
  X_IMAGE_REMOTE   rclone destination (default: personal-drive:X/asset-prompts)
  RCLONE_TRANSFERS parallel transfers (default: 8)
EOF
}

common=(--filter-from "$filter_file")

case "${1:-}" in
  upload)
    rclone copy "$repo_root" "$remote" "${common[@]}" \
      --checkers 16 --transfers "$transfers" --stats-one-line --stats 30s
    ;;
  download)
    rclone copy "$remote" "$repo_root" "${common[@]}" \
      --checkers 16 --transfers "$transfers" --stats-one-line --stats 30s
    ;;
  check)
    rclone check "$repo_root" "$remote" "${common[@]}" \
      --one-way --checkers 16
    ;;
  size-local)
    rclone size "$repo_root" "${common[@]}"
    ;;
  size-remote)
    rclone size "$remote" "${common[@]}"
    ;;
  -h|--help|help|"")
    usage
    ;;
  *)
    echo "Error: unknown command: $1" >&2
    usage >&2
    exit 2
    ;;
esac
