import os
import cv2
from moviepy.editor import VideoFileClip
from moviepy.editor import ImageSequenceClip
import Encoder

def get_video_fps(video_path):
    """Function to get the FPS of a video file."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return fps

# Function to convert video into frames and save them in a folder
def convert_video_to_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    # Read frames from the video and save them as images
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_folder, f"{frame_count}.png")
        cv2.imwrite(frame_path, frame)
        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()
    print(f"{frame_count} frames extracted and saved in '{output_folder}' folder.")

def combine_audio_video(video_path, og_path):
    """Combines an audio and a video object together"""
    capture = cv2.VideoCapture(og_path) # Stores OG Video into a Capture Window
    fps = capture.get(cv2.CAP_PROP_FPS) # Extracts FPS of OG Video

    video_path_real = video_path + "\\%d.png" # To Get All Frames in Folder

    os.system("ffmpeg-4.3.1-2020-10-01-full_build\\bin\\ffmpeg -framerate %s -i \"%s\" -codec copy output\\steg.mp4" % (str(int(fps)), video_path_real))
    
    print("Combining Complete!")

def combine_frames_to_video(frames_folder, output_video_path, fps):
    """Function to combine the encoded frames into a video."""
    # Get the list of frame file names
    frames_list = sorted(os.listdir(frames_folder))

    # Create a list of frame images
    frames = [os.path.join(frames_folder, frame) for frame in frames_list]

    # Load frames into a video clip
    video_clip = ImageSequenceClip(frames, fps=fps)

    # Write the video clip to the output path
    video_clip.write_videofile(output_video_path, codec='libx264')

    print(f"Video saved as {output_video_path}")

# Ask for the input video file path
video_file_path = "input/input_video.mp4"

# Ask for the input text file path
text_file_path = "input/message.txt"

# Convert video into frames and save them in a folder named 'frames'
frames_folder = "frames"
convert_video_to_frames(video_file_path, frames_folder)

# Get the total number of frames in the video
frame_count = len(os.listdir(frames_folder))

# Embed text into frames using Encoder.py logic
Encoder.encode(0, frame_count-1, text_file_path, frames_folder)

print("Steganography encoding completed.")

# Get the FPS of the original video
fps = get_video_fps(video_file_path)

# Combine encoded frames into a new video with the same FPS
output_video_path = "output/steg.mp4"  # Output video file path
# combine_frames_to_video(frames_folder, output_video_path, fps)
combine_audio_video(frames_folder,video_file_path)