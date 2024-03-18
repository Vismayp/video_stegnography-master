import os
import cv2
from PIL import Image
from Decoder import decode
from moviepy.editor import VideoFileClip

def get_input_path(prompt):
    """Function to prompt the user for a file path."""
    while True:
        file_path = input(prompt).strip()  # Get user input
        if os.path.isfile(file_path):  # Check if the file exists
            return file_path
        else:
            print("File not found. Please enter a valid file path.")

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

def get_frames(video_path):
    """Returns all frames in the video"""
    directory = "steg_frames"
    if not os.path.isdir(directory):
        os.makedirs(directory)
    
    video = VideoFileClip(video_path)
    
    for index, frame in enumerate(video.iter_frames()):
        img = Image.fromarray(frame, 'RGB')
        img.save(os.path.join(directory, f'{index}.png'))

# Ask for the input video file path
video_file_path = "input/encrypted_video_file.mp4"

# Convert steganographed video into frames and save them in a folder named 'steg_frames'
steg_frames_folder = "steg_frames"
# convert_video_to_frames(video_file_path, steg_frames_folder)
get_frames(video_file_path)

# Get the total number of frames in the steganographed video
frame_count = len(os.listdir(steg_frames_folder))

# Decode text from frames using Decoder.py logic
print("Extracting text from steganographed video...")
decoded_text = ""
for frame_number in range(frame_count-1):
    try:
        decoded_text += decode(frame_number, steg_frames_folder)
        print(f"Data found in Frame {frame_number}")
    except StopIteration:
        print(f"No data found in Frame {frame_number}")

# Save the decoded text to a file named 'recovered.txt'
output_text_file = "output/recovered.txt"
with open(output_text_file, "w") as file:
    file.write(decoded_text)

print("\nExtraction complete! Decoded text saved in 'recovered.txt'.")
