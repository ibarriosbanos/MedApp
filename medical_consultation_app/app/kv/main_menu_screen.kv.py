<MainMenuScreen>:
    canvas.before:
        Color:
            rgba: 0.9, 0.95, 0.9, 1  # Pastel background color
        Rectangle:
            pos: self.pos
            size: self.size

    GridLayout:
        cols: 2
        spacing: 20
        padding: 20

        Button:
            text: 'New Consultation'
            on_release:
                app.root.current = 'new_consultation_screen'
        Button:
            text: 'Existing Patients'
        Button:
            text: 'Medical Inquiry'
        Button:
            text: 'Learning'
        Button:
            text: 'Contact Other Doctors'
        Button:
            text: 'Settings'
