# Voice Recording Service

This microservice records an audio consultation and saves it as a `.wav` file. Once the recording is complete, it notifies the **Transcription Service** to begin transcription of the audio.

## Features:
- Records audio from the microphone using the `pyaudio` package.
- Saves the recording as a `.wav` file.
- Sends a request to the **Transcription Service** to start transcription after the recording is complete.

## Code Explanation:

### `record_audio()`
This function handles the audio recording process:
- **Chunk Size**: Audio is captured in chunks of 1024 samples at a time.
- **Format**: Records in 16-bit depth (`pyaudio.paInt16`).
- **Channels**: Mono recording (1 channel).
- **Rate**: Captures audio at a rate of 16 kHz.
- **Frames**: A list where all audio data is stored during recording.
- **Duration**: The recording duration is set to 60 seconds (but can be customized).
- **Saving the Audio**: The recorded audio is saved as a `.wav` file.

### `notify_transcription_service()`
After the recording is complete, this function sends an HTTP `POST` request to the **Transcription Service**:
- **URL**: The service sends the request to the `/transcribe` endpoint of the **Transcription Service** running on `localhost:5001`.
- **Data**: The audio file's name (`consultation.wav`) is sent as JSON in the request body.
- **Error Handling**: It catches any exceptions during the request to avoid crashes.

### Main Program
When the script is run, the main part of the program:
- **Records the Audio**: Calls the `record_audio()` function to record the consultation.
- **Notifies the Transcription Service**: Sends a request to the **Transcription Service** to start processing.

## How to Use:

1. **Install Dependencies**: Ensure you have the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Service**: You can start the voice recording service by running:

    ```bash
    python3 voice_recording_service.py
    ```

3. **Transcription Notification**: After the recording is complete, the service automatically sends the recorded audio file to the **Transcription Service** for processing.

## Dependencies:
- `pyaudio`: For capturing audio from the microphone.
- `wave`: For saving the recorded audio in `.wav` format.
- `requests`: For sending HTTP requests to the **Transcription Service**.
