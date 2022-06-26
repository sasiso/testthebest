import time

import win32api
import win32con
from pynput.mouse import Controller, Button

import find_template
import match_n_click
from match_n_click import MouseKeyboard


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


f = find_template.finder()


def click_on_position(x, y, which='left'):
    mouse.position = (x, y)

    time.sleep(.1)
    if which == "left":
        mouse.click(Button.left)

    elif which == 'right':
        mouse.click(Button.right)
    else:
        raise Exception('Not implemented')

    time.sleep(.5)


if __name__ == "__main__":
    mouse = Controller()
    mouse_keyboard = match_n_click.MouseKeyboard()
    mouse_keyboard.set_recording(True)
    print("Recording started")
    mouse_keyboard.do_record()

    while mouse_keyboard.get_recording():
        pass

    print("Recording finished")
    mouse_keyboard.stop_mouse_listner()

    mouse_keyboard.set_recording(True)

    print("Playing recording now")
    for i in range(200):

        print (f'loop number{i}')
        for l in mouse_keyboard.get_record():
            print(l)
            time.sleep(1)
            click_on_position(l.x, l.y, l.button)

        if not mouse_keyboard.get_recording():
            break
