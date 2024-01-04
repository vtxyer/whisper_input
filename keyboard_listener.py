import pynput
from multiprocessing import Event

class KeyboardListener:
    def __init__(self):
        self.ctrl_pressed = False
        self.alt_pressed = False
        self.start_recording = Event()
        self.stop_recording = Event()

    def on_press(self, key):
        if key == pynput.keyboard.Key.ctrl_l:
            self.ctrl_pressed = True
        elif key == pynput.keyboard.Key.alt_l:
            self.alt_pressed = True

        if self.ctrl_pressed and self.alt_pressed:
            # print("CTRL + ALT pressed")
            self.start_recording.set()
            self.stop_recording.clear()

    def on_release(self, key):
        if key == pynput.keyboard.Key.ctrl_l:
            self.ctrl_pressed = False
        elif key == pynput.keyboard.Key.alt_l:
            self.alt_pressed = False

        if not self.ctrl_pressed and not self.alt_pressed:
            # print("CTRL + ALT released")
            self.start_recording.clear()
            self.stop_recording.set()

    def listen(self):
        # Start listening for key events
        with pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            print("Listening...")
            listener.join()
