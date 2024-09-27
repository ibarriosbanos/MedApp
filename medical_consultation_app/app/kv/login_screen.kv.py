<LoginScreen>:
    canvas.before:
        Color:
            rgba: 0.9, 0.9, 0.95, 1  # Pastel background color
        Rectangle:
            pos: self.pos
            size: self.size

    FloatLayout:
        Label:
            text: 'Welcome to MedApp'
            font_size: 32
            pos_hint: {'center_x': 0.5, 'top': 0.9}
            color: (0, 0, 0, 1)

        TextInput:
            id: username
            hint_text: 'Username'
            size_hint: (0.8, 0.1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}

        TextInput:
            id: password
            hint_text: 'Password'
            password: True
            size_hint: (0.8, 0.1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.45}

        Button:
            text: 'Login'
            size_hint: (0.5, 0.1)
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            on_release:
                app.root.current = 'main_menu_screen'


