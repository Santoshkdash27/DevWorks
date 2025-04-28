# Video Transcoder

A simple batch video transcoder using FFmpeg and Python. Converts videos into different formats (MP4, MKV, AVI) based on user input.


## Features
- Converts videos in various formats (MP4, MKV, AVI).
- Batch processing: Converts multiple videos at once.
- Easy-to-use command-line interface.
- All PyCharm project files included, ready to be opened directly in PyCharm.

## Requirements
- Python 
- FFmpeg (Make sure FFmpeg is installed and accessible in your system's PATH)

### To install FFmpeg:
- **Windows**: Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add to the system PATH.
- **Mac/Linux**: You can install FFmpeg using package managers like `brew` or `apt`.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/Santoshkdash27/video-transcoder.git
    cd video-transcoder
    ```



3. Add your videos to the `./input_videos` folder.

4. Run the script:
    ```bash
    python transcode.py
    ```

5. When prompted, choose the format you want to convert your videos to:
    - 1: MP4
    - 2: MKV
    - 3: AVI

6. The converted videos will be saved in the `./output_videos` folder.


