<NewConsultationScreen>:
    canvas.before:
        Color:
            rgba: 0.95, 0.9, 0.9, 1  # Pastel background color
        Rectangle:
            pos: self.pos
            size: self.size

    FloatLayout:
        TextInput:
            id: date
            hint_text: 'Date'
            text: root.get_current_date()
            size_hint: (0.8, 0.08)
            pos_hint: {'center_x': 0.5, 'top': 0.9}
            multiline: False

        TextInput:
            id: place
            hint_text: 'Place'
            size_hint: (0.8, 0.08)
            pos_hint: {'center_x': 0.5, 'top': 0.8}
            multiline: False

        TextInput:
            id: patient_name
            hint_text: 'Patient Name'
            size_hint: (0.8, 0.08)
            pos_hint: {'center_x': 0.5, 'top': 0.7}
            multiline: False

        TextInput:
            id: patient_id
            hint_text: 'Patient ID'
            size_hint: (0.8, 0.08)
            pos_hint: {'center_x': 0.5, 'top': 0.6}
            multiline: False

        Button:
            text: 'Validate'
            size_hint: (0.5, 0.1)
            pos_hint: {'center_x': 0.5, 'top': 0.45}
            on_release:
                app.root.current = 'consultation_recording_screen'

