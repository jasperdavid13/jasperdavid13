import subprocess

def download_video(url):
    # Define the command for downloading the video
    command = [
        'yt-dlp',
        '--merge-output-format', 'mp4',  # Merge video and audio to mp4 format if separate
        '--format', 'bestvideo+bestaudio/best',  # Download best video and audio separately or best overall
        url
    ]
    
    # Run the command
    subprocess.run(command)

if __name__ == "__main__":
    # Replace the URL with the actual video URL you want to download
    video_url = "https://www.youtube.com/watch?v=sJnYUI6kVcQ"
    
    download_video(video_url)

print("File Saved Succesfully.Done!!")
