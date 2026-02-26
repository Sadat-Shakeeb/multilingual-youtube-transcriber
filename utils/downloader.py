import yt_dlp
import os


def download_audio(youtube_url, output_file="audio.mp3"):

    # Remove old audio if exists
    if os.path.exists(output_file):
        os.remove(output_file)

    if os.path.exists("temp_audio.mp3"):
        os.remove("temp_audio.mp3")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "temp_audio.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    if os.path.exists("temp_audio.mp3"):
        os.rename("temp_audio.mp3", output_file)

    return output_file