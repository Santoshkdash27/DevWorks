import os, subprocess, ffmpeg

def videoTranscoder(input_folder, output_folder):
    video_extensions = ('.mp4', '.mkv', '.avi')

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    all_files = os.listdir(input_folder)
    video_files = []

    for f_name in all_files:
        file_path = os.path.join(input_folder, f_name)
        if os.path.isfile(file_path) and f_name.endswith(video_extensions):
            video_files.append(f_name)

    print(f"Found {len(video_files)} video files.")


    print("Choose the format you want to convert to:")
    print("1: MP4")
    print("2: MKV")
    print("3: AVI")
    user_choice = input("Enter the number of the format: ")

    if user_choice == "1":
        output_extension = ".mp4"
        codec_video = "libx264"
        codec_audio = "aac"
    elif user_choice == "2":
        output_extension = ".mkv"
        codec_video = "libx264"
        codec_audio = "aac"
    elif user_choice == "3":
        output_extension = ".avi"
        codec_video = "libx264"
        codec_audio = "aac"
    else:
        print("Invalid choice! Defaulting to MP4.")
        output_extension = ".mp4"
        codec_video = "libx264"
        codec_audio = "aac"

    for video in video_files:
        try:
            input_path = os.path.join(input_folder, video)
            base_name = os.path.splitext(video)[0]
            output_path = os.path.join(output_folder, base_name + "_converted" + output_extension)

            command = ["ffmpeg", "-i", input_path, "-c:v", codec_video, "-preset", "fast", "-crf", "23", "-c:a", codec_audio, output_path]



            print(f"🔄 Converting: {video} to {output_extension.upper()} format...")
            subprocess.run(command, check=True)
            print(f"✅ Saved: {output_path}")

        except subprocess.CalledProcessError as e:
            print(f"❌ Error occurred while converting {video}: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")





input_folder = "./input_videos"
output_folder = "./output_videos"
videoTranscoder(input_folder, output_folder)




















