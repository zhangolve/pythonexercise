
# For uploading to YouTube
# H.264: smallest files
# This method uses libx264 to encode H.264 video. It is slower than the stream copy method below, but potentially will output a smaller file size.

# ffmpeg -loop 1 -framerate 1 -i image.jpg -i music.mp3 \
# -c:v libx264 -preset veryslow -crf 0 -c:a copy -shortest output.mkv

ffmpeg -loop 1 -framerate 1 -i abc.webp -i 001.mp3  -c:v libx264 -preset veryslow -crf 0 -c:a copy -shortest output.mkv
