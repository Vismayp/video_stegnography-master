from flask import Flask, Response, request, jsonify, send_from_directory, make_response
from flask_cors import CORS  # Import CORS from flask_cors
from werkzeug.utils import secure_filename
import os
import shutil
import time

app = Flask(__name__)
CORS(app) # Apply CORS to all routes

# Define upload folder
UPLOAD_FOLDER = 'input'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Define output folder
OUTPUT_FOLDER = 'output'
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Set allowed extensions
ALLOWED_EXTENSIONS = {'txt', 'mp4'}

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle file uploads
@app.route('/encoding/upload/mp4', methods=['POST'])
def upload_mp4_file_encoding():
    if 'file' not in request.files:
        return jsonify({'error': 'No MP4 file provided'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty MP4 file provided'})

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type provided'})

    filename = secure_filename('input_video.mp4')
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    print("Saved Video File")
    return jsonify({'message': 'MP4 file uploaded successfully', 'filename': filename})
 
# Route to handle file uploads
@app.route('/decoding/upload/mp4', methods=['POST'])
def upload_mp4_file_decoding():
    if 'file' not in request.files:
        return jsonify({'error': 'No MP4 file provided'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty MP4 file provided'})

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type provided'})

    filename = secure_filename('encrypted_video_file.mp4')
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    print("Saved Video File")
    return jsonify({'message': 'MP4 file uploaded successfully', 'filename': filename})

# Route to handle text file uploads
@app.route('/encoding/upload/text', methods=['POST'])
def upload_text_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No text file provided'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty text file provided'})

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type provided'})

    filename = secure_filename('message.txt')
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    print("saved text file")
    return jsonify({'message': 'Text file uploaded successfully', 'filename': filename})

# Route to retrieve output file
@app.route('/encoding/start', methods=['GET'])
def get_output_file_for_encoding():
    print("Starting Program...\n")
    os.system("python Module1.py")
    print("Execution completed.")
    return jsonify({'message': 'Execution completed',})

# Route to retrieve output file
@app.route('/decoding/start', methods=['GET'])
def get_output_file_for_decoding():
    print("Starting Program...\n")
    os.system("python Module2.py")
    print("Execution completed.")
    return jsonify({'message': 'Execution completed',})

# Route to retrieve output file
@app.route('/encoding/output', methods=['GET'])
def get_video_output():
    mp4_files = [f for f in os.listdir(OUTPUT_FOLDER) if f.endswith('.mp4')]
    if not mp4_files:
        return jsonify({'error': 'No MP4 file found in output directory'})

    first_mp4_file = mp4_files[0]
    filepath = os.path.join(OUTPUT_FOLDER, first_mp4_file)

    response = make_response(send_from_directory(OUTPUT_FOLDER, first_mp4_file))
    response.headers['Content-Disposition'] = f'attachment; filename="{first_mp4_file}"'
    return response

# Route to retrieve output file
@app.route('/decoding/output', methods=['GET'])
def get_text_output():
    txt_files = [f for f in os.listdir(OUTPUT_FOLDER) if f.endswith('.txt')]
    if not txt_files:
        return jsonify({'error': 'No Text file found in output directory'})

    first_txt_file = txt_files[0]
    filepath = os.path.join(OUTPUT_FOLDER, first_txt_file)

    response = make_response(send_from_directory(OUTPUT_FOLDER, first_txt_file))
    response.headers['Content-Disposition'] = f'attachment; filename="{first_txt_file}"'
    return response

if __name__ == '__main__':
    app.run(debug=True)
