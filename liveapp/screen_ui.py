from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFlatButton

class ScreenUI(Screen):
    def __init__(self):
        super().__init__()
        mdflat_button = MDFlatButton(
            text="This is an autoreload application",
            pos_hint={"center_x": .5, "center_y":.5}
        )
        self.add_widget(mdflat_button)
