from flask import Flask, request, jsonify
import speech_recognition as sr
from pydub import AudioSegment
import requests
import os

app = Flask(__name__)

# Route to receive audio file and transcribe it
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    data = request.get_json()

    # Extract the audio file name from the incoming request
    audio_file = data.get('audio_file')

    # Check if the audio file exists
    if not os.path.exists(audio_file):
        return jsonify({'error': 'Audio file not found'}), 404

    # Convert audio file to the correct format (if necessary) using pydub
    audio = AudioSegment.from_file(audio_file)
    audio.export("temp.wav", format="wav")

    # Perform transcription
    transcription = transcribe("temp.wav")

    if not transcription:
        return jsonify({'error': 'Transcription failed'}), 500

    # Send the transcription to the Summary Service
    notify_summary_service(transcription)

    return jsonify({
        'status': 'Transcription completed',
        'transcription': transcription
    })

# Function to perform speech recognition on the audio file
def transcribe(audio_file):
    recognizer = sr.Recognizer()

    # Open the audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

        try:
            # Perform speech recognition using Google's API (for simplicity)
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

# Function to send the transcription to the Summary Service
def notify_summary_service(transcription):
    url = 'http://localhost:5002/summarize'  # Summary Service endpoint
    data = {'transcription': transcription}

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Successfully sent transcription to Summary Service. Response: {response.json()}")
        else:
            print(f"Failed to send transcription to Summary Service. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request to Summary Service: {e}")

# Start the Flask server
if __name__ == "__main__":
    app.run(port=5001)
