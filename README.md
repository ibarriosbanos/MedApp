# Medical Consultation App

## Voice Recording Service

This microservice records an audio consultation and saves it as a `.wav` file. Once the recording is complete, it notifies the **Transcription Service** to begin transcription of the audio.

### Features:
- Records audio from the microphone using the `pyaudio` package.
- Saves the recording as a `.wav` file.
- Sends a request to the **Transcription Service** to start transcription after the recording is complete.

### Code Explanation:

#### `record_audio()`
This function handles the audio recording process:
- **Chunk Size**: Audio is captured in chunks of 1024 samples at a time.
- **Format**: Records in 16-bit depth (`pyaudio.paInt16`).
- **Channels**: Mono recording (1 channel).
- **Rate**: Captures audio at a rate of 16 kHz.
- **Frames**: A list where all audio data is stored during recording.
- **Duration**: The recording duration is set to 60 seconds (but can be customized).
- **Saving the Audio**: The recorded audio is saved as a `.wav` file.

#### `notify_transcription_service()`
After the recording is complete, this function sends an HTTP `POST` request to the **Transcription Service**:
- **URL**: The service sends the request to the `/transcribe` endpoint of the **Transcription Service** running on `localhost:5001`.
- **Data**: The audio file's name (`consultation.wav`) is sent as JSON in the request body.
- **Error Handling**: It catches any exceptions during the request to avoid crashes.

#### Main Program
When the script is run, the main part of the program:
- **Records the Audio**: Calls the `record_audio()` function to record the consultation.
- **Notifies the Transcription Service**: Sends a request to the **Transcription Service** to start processing.

### How to Use:

1. **Install Dependencies**: Ensure you have the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Service**: You can start the voice recording service by running:

    ```bash
    python3 voice_recording_service.py
    ```

3. **Transcription Notification**: After the recording is complete, the service automatically sends the recorded audio file to the **Transcription Service** for processing.

### Dependencies:
- `pyaudio`: For capturing audio from the microphone.
- `wave`: For saving the recorded audio in `.wav` format.
- `requests`: For sending HTTP requests to the **Transcription Service**.

## Transcription Service

This microservice receives an audio file from the **Voice Recording Service**, transcribes it into text, and sends the transcription to the **Summary Service** for further processing.

### Features:
- Receives an audio file from the **Voice Recording Service**.
- Converts the audio file into text using the `SpeechRecognition` library.
- Sends the transcribed text to the **Summary Service** for further processing.

### Code Explanation:
- **`transcribe_audio()`**: This function handles the main logic:
  - Receives the audio file from the **Voice Recording Service**.
  - Uses `pydub` to convert the audio file to the correct format (WAV).
  - Uses the `SpeechRecognition` library to transcribe the audio into text.
  - Sends the transcription to the **Summary Service**.
  
- **`transcribe()`**: This function handles speech recognition:
  - Loads the audio file.
  - Uses Google's Speech Recognition API to transcribe the audio into text.

- **`notify_summary_service()`**: Sends the transcription to the **Summary Service** via an HTTP POST request.

### How to Use:
1. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2. **Run the Service**:
    ```bash
    python3 transcription_service.py
    ```
3. The service will listen for transcription requests from the **Voice Recording Service**.

### Dependencies:
- `flask`: For creating the API server.
- `SpeechRecognition`: For speech-to-text functionality.
- `pydub`: For handling audio files.
- `requests`: For sending the transcription to the **Summary Service**.

---

## Summary Service

This microservice receives a transcription from the **Transcription Service**, extracts symptoms and measurements, and sends a structured summary to the **Diagnosis Service** for further processing.

### Features:
- Receives a transcription of the consultation from the **Transcription Service**.
- Extracts common symptoms (e.g., fever, cough) and measurements (e.g., temperature, blood pressure).
- Sends the structured summary to the **Diagnosis Service**.

### Code Explanation:
- **`summarize()`**: Main function to receive transcription and extract information:
  - Receives transcription as input.
  - Extracts symptoms and measurements using text processing and regex.
  - Sends the structured summary to the **Diagnosis Service**.
  
- **`extract_symptoms()`**: Extracts common symptoms based on a predefined list (can be expanded as needed).

- **`extract_measurements()`**: Uses regular expressions to extract specific measurements like temperature and blood pressure.

- **`notify_diagnosis_service()`**: Sends the structured summary to the **Diagnosis Service** via an HTTP POST request.

### How to Use:
1. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2. **Run the Service**:
    ```bash
    python3 summary_service.py
    ```
3. The service will listen for transcription data from the **Transcription Service**.

### Dependencies:
- `flask`: For creating the API server.
- `nltk`: For simple natural language processing.
- `requests`: For sending the summary to the **Diagnosis Service**.

---

## Diagnosis Service

This microservice receives a structured summary of symptoms and measurements from the **Summary Service**, generates a possible diagnosis using a language model (e.g., OpenAI's GPT), and suggests treatments based on the diagnosis.

### Features:
- Receives structured data (symptoms and measurements) from the **Summary Service**.
- Uses a language model (like GPT) to generate a possible diagnosis and suggest treatments.
- Returns the diagnosis and treatment suggestions as a JSON response.

### Code Explanation:
- **`diagnose()`**: Main function to receive the summary and generate a diagnosis:
  - Receives symptoms and measurements as input.
  - Creates a prompt using the provided data.
  - Sends the prompt to the language model (e.g., OpenAI’s GPT) to get a diagnosis.
  - Saves the diagnosis to a file and returns it as a response.
  
- **`create_prompt()`**: Creates a prompt for the language model based on the symptoms and measurements.

- **`get_diagnosis()`**: Sends the prompt to the language model (e.g., GPT) and returns the diagnosis.

### How to Use:
1. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2. **Set up your OpenAI API key** as an environment variable:
    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    ```
3. **Run the Service**:
    ```bash
    python3 diagnosis_service.py
    ```
4. The service will listen for structured summaries from the **Summary Service**.

### Dependencies:
- `flask`: For creating the API server.
- `openai`: For interacting with the OpenAI API (or another LLM).
- `requests`: For receiving the summary and returning the diagnosis.

