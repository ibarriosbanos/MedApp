<ConsultationRecordingScreen>:
    canvas.before:
        Color:
            rgba: 0.9, 0.95, 0.95, 1  # Pastel background color
        Rectangle:
            pos: self.pos
            size: self.size

    FloatLayout:
        Label:
            id: patient_label
            text: 'Consultation with '
            font_size: 24
            pos_hint: {'center_x': 0.5, 'top': 0.95}
            color: (0, 0, 0, 1)

        Button:
            id: record_button
            text: 'Start Recording'
            size_hint: (0.6, 0.1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            on_release:
                root.toggle_recording()

        Button:
            text: 'Finish'
            size_hint: (0.4, 0.1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            on_release:
                root.finish_recording()
