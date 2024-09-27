from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from datetime import datetime

Builder.load_file('kv/new_consultation_screen.kv')

class NewConsultationScreen(Screen):
    def get_current_date(self):
        return datetime.now().strftime('%Y-%m-%d')

