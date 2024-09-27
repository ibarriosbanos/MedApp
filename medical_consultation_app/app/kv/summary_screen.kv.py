<SummaryScreen>:
    canvas.before:
        Color:
            rgba: 0.95, 0.95, 0.9, 1  # Pastel background color
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20

        Label:
            text: 'Consultation Summary'
            font_size: 24

        ScrollView:
            TextInput:
                id: summary_text
                text: root.transcription_summary
                readonly: True
                size_hint_y: None
                height: self.minimum_height
                font_size: 18

        BoxLayout:
            size_hint_y: None
            height: 50
            spacing: 10

            Button:
                text: 'Edit Manually'
                on_release:
                    summary_text.readonly = False

            Button:
                text: 'Push to CRM'

            Button:
                text: 'Get Diagnosis'
                on_release:
                    root.get_diagnosis()

            Button:
                text: 'Discard/Delete'
                on_release:
                    app.root.current = 'main_menu_screen'
