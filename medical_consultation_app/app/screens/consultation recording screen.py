from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import threading
import pyaudio
import wave
import requests

Builder.load_file('kv/consultation_recording_screen.kv')

class ConsultationRecordingScreen(Screen):
    recording = False
    frames = []
    stream = None
    p = None
    patient_name = ''

    def on_enter(self):
        # Get patient name from the previous screen
        self.patient_name = self.manager.get_screen('new_consultation_screen').ids.patient_name.text
        self.ids.patient_label.text = f'Consultation with {self.patient_name}'

    def toggle_recording(self):
        if not self.recording:
            self.ids.record_button.text = 'Stop Recording'
            self.recording = True
            threading.Thread(target=self.start_recording).start()
        else:
            self.ids.record_button.text = 'Resume Recording'
            self.recording = False
            self.stop_recording()

    def start_recording(self):
        self.frames = []
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 16000
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.format,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)
        while self.recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

    def stop_recording(self):
        self.recording = False
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        if self.p is not None:
            self.p.terminate()
        self.save_recording()

    def save_recording(self):
        wf = wave.open('consultation.wav', 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        self.notify_transcription_service()

    def notify_transcription_service(self):
        data = {'audio_file': 'consultation.wav'}
        try:
            response = requests.post('http://localhost:5001/transcribe', json=data)
            if response.status_code == 200:
                print('Transcription started.')
            else:
                print('Failed to start transcription.')
        except Exception as e:
            print(f'Error: {e}')

    def finish_recording(self):
        if self.recording:
            self.stop_recording()
        app = App.get_running_app()
        app.root.current = 'summary_screen'

