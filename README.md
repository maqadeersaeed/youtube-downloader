# YouTube Shorts Downloader

## Overview

This project provides a Python-based tool to download YouTube Shorts videos in high quality (up to 1080p) using the `yt-dlp` library. The tool automates video downloads with features such as virtual environment setup and dependency installation.

## Features

- Download YouTube Shorts videos in the highest available resolution (up to 1080p).
- Retry mechanism for downloading videos with fallback to lower resolutions if 1080p is unavailable.
- Uses virtual environments for dependency isolation.
- Batch scripts for easy environment setup and running the project.

## Limitations

- The tool relies on the `yt-dlp` library, which may require updates to handle YouTube’s frequent API changes.
- Requires `ffmpeg` to merge audio and video streams when necessary.
- May not work with certain videos due to restrictions like region-locking, age-restrictions, or private content.
- The download speed and availability depend on YouTube’s policies and server limitations.

## Risks Associated

- Overuse or bulk downloading may lead to account suspension or IP blocking by YouTube.
- Unauthorized use of copyrighted content may result in legal consequences.

## Setup and Run Instructions

### Prerequisites

1. Ensure Python 3.8 or higher is installed on your system.
2. Install `ffmpeg` for merging audio and video streams.

### Installing `ffmpeg` on Windows

1. **Download FFmpeg**:
   - Visit the [official FFmpeg download page](https://www.ffmpeg.org/download.html) or download a Windows build from [Gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
   - Download the "essentials" or "full" build.

2. **Extract FFmpeg**:
   - Extract the downloaded ZIP file to a folder, for example, `C:\ffmpeg`.

3. **Add FFmpeg to System PATH**:
   - Open the Start Menu and search for "Environment Variables."
   - Click on "Edit the system environment variables."
   - In the System Properties window, click "Environment Variables."
   - Under "System variables," find the `Path` variable and click "Edit."
   - Click "New" and add the path to the `bin` folder inside the FFmpeg directory, e.g., `C:\ffmpeg\bin`.
   - Click "OK" to close all windows.

4. **Verify Installation**:
   - Open Command Prompt and type `ffmpeg -version`.
   - You should see FFmpeg's version information, confirming that it is installed correctly.

### Setup

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the following command to set up the environment:
   ```
   setup_env.bat
   ```
   This creates a virtual environment and installs the required dependencies from `requirements.txt`.

### Running the Project

1. Place the list of YouTube Shorts video URLs in a file named `youtube_shorts_links.txt`, one URL per line.
2. Run the following command to start downloading:
   ```
   run.bat
   ```
3. The script will activate the virtual environment and download the videos listed in the `youtube_shorts_links.txt` file.

### Output

- Downloaded videos will be saved in the `downloaded_videos/` folder within the project directory.

## Disclaimer

This project is for educational purposes only. The intent is to help users learn about automation and Python scripting. Use this tool responsibly and fairly without violating YouTube’s terms of service or misusing copyrighted content. The author is not liable for any misuse of this code by others.

## Fair Use Notice

- Avoid exploiting YouTube by bulk downloading content or redistributing videos without permission.
- Respect intellectual property rights and use this tool for personal or non-commercial educational purposes only.

## Acknowledgments

- `yt-dlp` library for simplifying the video downloading process.
- Open-source contributors for their efforts in maintaining supporting tools and libraries.

