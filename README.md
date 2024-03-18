Steganography Project

Overview
This project implements steganography, a technique of hiding secret data within an ordinary, non-secret file or message to avoid detection. The project consists of two modules: one for encoding data into a video file and another for decoding the hidden data from the steganographed video.

Modules
Module 1: Steganography Encoder
* Accepts the path to the input video file.
* Accepts the path to the text file that contains the data to be embedded.
* Converts the video into frames.
* Embeds the text data into the frames using the provided Encoder logic.
* Combines the frames with embedded data to create a new video.
* Outputs the steganographed video.

Module 2: Steganography Decoder
* Accepts the path to the steganographed video file.
* Converts the steganographed video into frames.
* Utilizes the provided Decoder logic to extract the hidden text from the frames.
* Saves the extracted text to a file.

Requirements
* Python 3.x
* OpenCV
* Pillow (PIL)
* moviepy

pip install opencv-python pillow moviepy
Ensure that ffmpeg is installed and available in the system path.

Usage

Module 1: Steganography Encoder
Run the Module1.py script.
Follow the prompts to provide the input video file path and the text file containing the data to be embedded.
The script will convert the video into frames, embed the text data, and generate the steganographed video.


Module 2: Steganography Decoder
Run the Module2.py script.
Enter the path to the steganographed video file.
The script will extract the hidden text from the video frames and save it to a file named recovered.txt.


Authors
Author 1 KrishnaKumar K- 211IT034
Author 2 RD Karthik - 211IT030
Aurthor 3 Vismay P - 211IT083