import os
import yt_dlp
import time

def download_videos(file_path, output_folder):
    try:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return
        
        os.makedirs(output_folder, exist_ok=True)

        with open(file_path, 'r') as file:
            links = file.readlines()
        
        if not links:
            print("No links found in the file.")
            return
        
        for idx, link in enumerate(links):
            link = link.strip()
            if not link:
                continue
            
            try:
                print(f"Processing: {link}")
                ydl_opts = {
                    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
                    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
                    'quiet': False,
                    'merge_output_format': 'mp4',
                    'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
                    }
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                print(f"Downloaded {idx + 1}/{len(links)}: {link}")
            
            except Exception as e:
                print(f"Error downloading video {idx + 1}: {link}. Error: {e}")
            
            # Wait for 10 seconds before processing the next link
            time.sleep(10)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "youtube_shorts_links.txt")
    output_folder = os.path.join(script_dir, "downloaded_videos")
    download_videos(file_path, output_folder)
