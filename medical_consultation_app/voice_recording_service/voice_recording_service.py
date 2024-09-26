import pyaudio
import wave
import requests

# Function to record audio and save it as a WAV file, which will later be converted to MP3
def record_audio(output_filename, record_seconds=60):
    # Set chunk size of 1024 samples per data frame
    chunk = 1024
    
    # Set the audio format - 16 bits per sample
    format = pyaudio.paInt16

    # Mono audio recording (1 channel)
    channels = 1

    # Recording rate at 16kHz (16000 samples per second)
    rate = 16000

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open the stream for audio input
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")

    # List to hold the recorded frames
    frames = []

    # Record the audio for the given duration (in seconds)
    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)  # Read audio data
        frames.append(data)  # Append audio data to frames list

    print("Finished recording.")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    
    # Terminate the PortAudio interface
    p.terminate()

    # Save the audio as a WAV file
    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(channels)  # Set number of channels
    wf.setsampwidth(p.get_sample_size(format))  # Set sample width
    wf.setframerate(rate)  # Set the frame rate
    wf.writeframes(b''.join(frames))  # Write the frames to the file
    wf.close()

    # After recording, send a request to the Transcription Service to start transcription
    notify_transcription_service(output_filename)

# Function to send a request to the Transcription Service
def notify_transcription_service(audio_file):
    url = 'http://localhost:5001/transcribe'  # Transcription service endpoint
    data = {'audio_file': audio_file}  # Data to send (audio file name)

    try:
        # Send a POST request to notify the Transcription Service
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Successfully notified the Transcription Service. Response: {response.json()}")
        else:
            print(f"Failed to notify the Transcription Service. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending request to Transcription Service: {e}")

# Main entry point for the Voice Recording Service
if __name__ == "__main__":
    # Record the consultation and save it as 'consultation.wav' for a duration of 60 seconds
    record_audio('consultation.wav', record_seconds=60)
