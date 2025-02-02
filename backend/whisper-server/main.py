import os
import tempfile
import whisper
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Initialize the whisper model
model = whisper.load_model("base")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # Ensure the file is not empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(file.read())  # Save the file
            temp_file_path = temp_file.name  # Get the file path

        # Run whisper's transcription
        result = model.transcribe(temp_file_path)

        # Clean up the temporary file
        os.unlink(temp_file_path)

        return jsonify({
            "message": "Transcription successful",
            "transcription": result['text']
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health-check', methods=['GET'])
def health_check():
    return jsonify({"status": "Working fine"})

if __name__ == '__main__':
    app.run(debug=True)
