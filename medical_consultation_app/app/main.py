from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# Import screen classes
from screens.login_screen import LoginScreen
from screens.main_menu_screen import MainMenuScreen
from screens.new_consultation_screen import NewConsultationScreen
from screens.consultation_recording_screen import ConsultationRecordingScreen
from screens.summary_screen import SummaryScreen

class MedApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(MainMenuScreen(name='main_menu_screen'))
        sm.add_widget(NewConsultationScreen(name='new_consultation_screen'))
        sm.add_widget(ConsultationRecordingScreen(name='consultation_recording_screen'))
        sm.add_widget(SummaryScreen(name='summary_screen'))
        return sm

if __name__ == '__main__':
    MedApp().run()
