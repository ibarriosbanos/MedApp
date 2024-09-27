<LoginScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20

        Label:
            text: 'Welcome to MedApp'
            font_size: 32
            color: (0, 0, 0, 1)

        TextInput:
            id: username
            hint_text: 'Username'
            multiline: False

        TextInput:
            id: password
            hint_text: 'Password'
            password: True
            multiline: False

        Button:
            text: 'Login'
            size_hint: (1, 0.5)
            on_release:
                app.root.current = 'main_menu'

<LoginScreen>:
    canvas.before:
        Color:
            rgba: 0.9, 0.9, 0.95, 1  # Pastel background color
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        # (Same as before)