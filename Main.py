from pytube import YouTube

# Step 1: Create a YouTube object
video_url = "https://www.youtube.com/watch?v=KHowZAYWAvc"
yt = YouTube(video_url)

# Step 2: Choose a video and audio stream to download
video_stream = yt.streams.get_highest_resolution()
audio_stream = yt.streams.get_audio_only()

# Step 3: Download the video and audio streams
video_stream.download(output_path="path/to/download/directory")
audio_stream.download(output_path="path/to/download/directory")
