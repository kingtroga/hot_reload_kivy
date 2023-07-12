# HOW TO USE HOT RELOADS IN WINDOWS
1. To use HOT RELOADS with '''Kivy/KivyMD''', you need to have ```kaki``` installed. This can be done using ```pip```:
```pip install kaki```
2. Set up your '''Kivy/KivyMD''' project's "main.py" file similar to mine. That is:
- and the names and locations of all the classes in your app to the ```CLASSES``` constant variable like so:```CLASSES = {
        "ScreenUI":"liveapp.screen_ui"
    }```
3. Next set all the paths in your project in the constast variable ```AUTORELOADER_PATHS``` to reload automatically like so:```AUTORELOADER_PATH = [(".", {"recursive": True})]```
4. Next define the ```build_app()``` function in your you app it takes two arguments, ```self``` and ```*args``` and it must return the entry point, usually a ScreenManager Class, into your app like so ```...return Factory.ScreenUI()```. Check the ```main.py``` file for more details
5. Finally, after and the ```...run()``` to your main.py file. To run it on windows in HOT RELOADS from here is the '''CMD''' command:
```set DEBUG=1 && python3 main.py```
HAVE FUN BUILDING👋