from flask import Flask, request, jsonify
import re
import json
import requests
import nltk

# Download NLTK data (only needs to be done once)
nltk.download('punkt')

app = Flask(__name__)

# Route to receive transcription data and create a summary
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()

    # Extract the transcription text from the incoming data
    transcription = data.get('transcription', '')

    # Extract symptoms and measurements from the transcription
    symptoms = extract_symptoms(transcription)
    measurements = extract_measurements(transcription)

    # Create a structured summary
    summary = {
        'symptoms': symptoms,
        'measurements': measurements
    }

    # Save the summary to a JSON file (optional, for development purposes)
    with open('summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=4)

    # Send the summary to the Diagnosis Service
    notify_diagnosis_service(summary)

    # Return the summary as a JSON response
    return jsonify({
        'status': 'Summary completed',
        'summary': summary
    })

# Function to extract symptoms from the transcription
def extract_symptoms(text):
    # A simple list of common symptoms for demo purposes (can be expanded)
    symptom_list = ['fever', 'cough', 'headache', 'fatigue', 'sore throat', 'shortness of breath']
    
    # Find symptoms present in the transcription
    symptoms_found = [symptom for symptom in symptom_list if symptom in text.lower()]
    return symptoms_found

# Function to extract measurements (like temperature, blood pressure, etc.)
def extract_measurements(text):
    measurements = {}

    # Use regular expressions to find temperature (e.g., "38.5°C")
    temp_match = re.search(r'([3-4][0-9]\.[0-9])\s*°?C', text)
    if temp_match:
        measurements['temperature'] = temp_match.group(1)

    # Use regular expressions to find blood pressure (e.g., "120/80")
    bp_match = re.search(r'(\d{2,3}/\d{2,3})', text)
    if bp_match:
        measurements['blood_pressure'] = bp_match.group(1)

    return measurements

# Function to notify the Diagnosis Service by sending the summary
def notify_diagnosis_service(summary):
    url = 'http://localhost:5003/diagnose'  # Diagnosis Service endpoint
    try:
        response = requests.post(url, json=summary)
        if response.status_code == 200:
            print(f"Successfully sent summary to Diagnosis Service. Response: {response.json()}")
        else:
            print(f"Failed to send summary to Diagnosis Service. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request to Diagnosis Service: {e}")

# Start the Flask server
if __name__ == "__main__":
    app.run(port=5002)
