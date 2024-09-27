from flask import Flask, request, jsonify
import openai
import json
import os

app = Flask(__name__)

# Load your OpenAI API key from environment variables for security
openai.api_key = os.getenv('OPENAI_API_KEY')

# Main route to receive the summary data (symptoms and measurements) and return a diagnosis
@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()

    # Extract symptoms and measurements from the incoming request
    symptoms = data.get('symptoms', [])
    measurements = data.get('measurements', {})

    # Create a prompt based on the symptoms and measurements
    prompt = create_prompt(symptoms, measurements)
    
    # Get a diagnosis from GPT or another LLM
    diagnosis = get_diagnosis(prompt)

    # Log the diagnosis (for development and debugging purposes)
    print("Diagnosis: ", diagnosis)

    # Save the diagnosis to a text file (optional, can be removed)
    with open('diagnosis.txt', 'w', encoding='utf-8') as f:
        f.write(diagnosis)

    # Return the diagnosis and treatment suggestions as a JSON response
    return jsonify({
        'diagnosis': diagnosis
    })

# Function to create the prompt for the LLM
def create_prompt(symptoms, measurements):
    prompt = "The patient presents the following symptoms:\n"
    for symptom in symptoms:
        prompt += f"- {symptom}\n"
    
    prompt += "The measurements are:\n"
    for key, value in measurements.items():
        prompt += f"- {key}: {value}\n"

    # Ask for a diagnosis and potential treatment
    prompt += "\nBased on the symptoms and measurements, provide a possible diagnosis and suggest treatments. Use medical references like Medimecum or trusted sources."
    
    return prompt

# Function to get the diagnosis from GPT (or another LLM)
def get_diagnosis(prompt):
    try:
        # Query the OpenAI GPT model
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify the engine you want to use
            prompt=prompt,
            max_tokens=500,
            temperature=0.7,  # Adjust temperature for creativity vs. accuracy
            n=1
        )
        return response.choices[0].text.strip()  # Return the text response
    except Exception as e:
        print(f"Error getting diagnosis: {e}")
        return "Sorry, there was an error generating the diagnosis."

# Start the Flask server
if __name__ == "__main__":
    app.run(port=5003)
