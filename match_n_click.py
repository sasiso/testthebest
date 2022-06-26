import threading
import tkinter as tk

from pynput import keyboard
from pynput.mouse import Listener


class CilckInfo:
    def __init__(self, button, x, y):
        self.button = button
        self.x = x
        self.y = y

    def __str__(self):
        return f'CilckInfo button ={self.button}, x = {self.x}, y = {self.y}'

    def __repr__(self):
        return f'CilckInfo button ={self.button}, x = {self.x}, y = {self.y}'


class MouseKeyboard:

    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-alpha', 0.5)
        self.root.attributes("-topmost", True)
        self.x = 0
        self.y = 0
        self.updated = False
        self.processing = False
        self.recording = False
        self.record = []
        print(threading.get_ident())
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def get_record(self):
        return self.record

    def center_window(self, width=300, height=200, x=0, y=0):
        # calculate position x and y coordinates
        print(x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def stop_mouse_listner(self):
        self.l.stop()

    def set_recording(self, flag):

        self.recording = flag

    def get_recording(self):
        return self.recording

    def on_click(self, x1, y1, button, pressed):
        print(threading.get_ident())

        if self.processing:
            return

        if self.recording:
            if pressed:
                print("Recording", button)
                c = CilckInfo(button=button.name, x=x1, y=y1)
                self.record.append(c)
                print(self.record)
                print(len(self.record))
                return

        if self.processing:
            return

        self.processing = True
        print(threading.get_ident())
        if pressed:
            self.updated = True
            self.x = x1
            vy = y1
        self.processing = False

    def stop_recording(self):
        self.recording = False

    def on_press(self, key):
        global recording
        self.stop_recording()
        print(self.record)
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(self, key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def do_record(self):
        global recording
        recording = True

        self.l = Listener(on_click=self.on_click)
        self.l.start()

    def do_processing(self, x_in, y_in):

        if self.updated:
            self.center_window(100, 100, x_in, y_in)
            self.root.lift()
            self.updated = False
        self.root.update_idletasks()
        self.root.update_idletasks()
        self.root.update()


if __name__ == "__main__":
    do_record()

    while True:
        if updated:
            center_window(100, 100, x, y)
            root.lift()
            updated = False
        root.update_idletasks()
        root.update()
