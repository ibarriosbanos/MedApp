from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import threading
import requests
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App

Builder.load_file('kv/summary_screen.kv')

class SummaryScreen(Screen):
    transcription_summary = ''

    def on_enter(self):
        self.transcription_summary = 'Waiting for transcription...'
        self.ids.summary_text.text = self.transcription_summary
        threading.Thread(target=self.get_summary).start()

    def get_summary(self):
        # Simulate waiting for the transcription and summary
        import time
        time.sleep(5)  # Simulate processing time
        # In a real scenario, you would poll or receive a callback from the summary service
        self.transcription_summary = 'This is the transcribed and summarized consultation.'
        self.ids.summary_text.text = self.transcription_summary

    def get_diagnosis(self):
        data = {'summary': self.transcription_summary}
        try:
            response = requests.post('http://localhost:5003/diagnose', json=data)
            if response.status_code == 200:
                diagnosis = response.json().get('diagnosis', '')
                self.show_popup('Diagnosis', diagnosis)
            else:
                self.show_popup('Error', 'Failed to get diagnosis.')
        except Exception as e:
            self.show_popup('Error', str(e))

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(0.8, 0.8))
        popup.open()

