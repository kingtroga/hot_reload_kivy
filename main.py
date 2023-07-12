from kaki.app import App
from kivymd.app import MDApp 
from kivy.factory import Factory
from kivy.core.window import Window

Window.size = (360, 548)



class MDLiveKaki(App, MDApp):

    CLASSES = {
        "ScreenUI":"liveapp.screen_ui"
    }

    AUTORELOADER_PATHS = [
        (".", {"recursive": True})
    ]

    def build_app(self, *args):
        print("Inside Build app auto Reload4")
        return Factory.ScreenUI()

MDLiveKaki().run()