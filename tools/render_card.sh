#!/usr/bin/env bash
# Renders assets/linkedin-card/card.html into gadfly-card.gif and gadfly-card.mp4.
# Needs google-chrome and ffmpeg. Usage: tools/render_card.sh [work_dir]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/assets/linkedin-card"
WORK="${1:-$(mktemp -d)}"
FPS=15
LOOP=9
FRAMES=$((FPS * LOOP))

mkdir -p "$WORK/frames"

render_frame() {
  local i="$1" t
  t=$(awk -v i="$i" -v fps="$FPS" 'BEGIN{printf "%.4f", i/fps}')
  google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
    --window-size=1200,627 \
    --user-data-dir="$WORK/profile-$i" \
    --screenshot="$WORK/frames/$(printf '%04d' "$i").png" \
    "file://$SRC/card.html?t=$t" >/dev/null 2>&1
  rm -rf "$WORK/profile-$i"
}
export -f render_frame
export SRC WORK FPS

seq 0 $((FRAMES - 1)) | xargs -P 6 -I{} bash -c 'render_frame {}'

ffmpeg -y -loglevel error -framerate "$FPS" -i "$WORK/frames/%04d.png" \
  -vf "palettegen=max_colors=128:stats_mode=diff" "$WORK/palette.png"
ffmpeg -y -loglevel error -framerate "$FPS" -i "$WORK/frames/%04d.png" -i "$WORK/palette.png" \
  -lavfi "paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" -loop 0 "$SRC/gadfly-card.gif"
ffmpeg -y -loglevel error -framerate "$FPS" -stream_loop 2 -i "$WORK/frames/%04d.png" \
  -vf "pad=1200:628:0:0:color=0x171B1D" -c:v libx264 -pix_fmt yuv420p -crf 20 -movflags +faststart "$SRC/gadfly-card.mp4"

ls -la "$SRC"/gadfly-card.*
