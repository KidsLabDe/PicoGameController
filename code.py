import time
import board
import digitalio


import usb_hid
from adafruit_hid.keyboard import Keyboard
# from keyboard_layout_win_de import KeyboardLayout
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
# layout = KeyboardLayout(keyboard)


def typeIt(string):
        layout.write(string)


debug = False

btn_up_pin      = board.GP15
btn_down_pin    = board.GP17
btn_left_pin    = board.GP14
btn_right_pin   = board.GP16
btn_click_pin   = board.GP18

btn_up_pin = digitalio.DigitalInOut(btn_up_pin)
btn_up_pin.direction = digitalio.Direction.INPUT
btn_up_pin.pull = digitalio.Pull.DOWN

btn_down_pin = digitalio.DigitalInOut(btn_down_pin)
btn_down_pin.direction = digitalio.Direction.INPUT
btn_down_pin.pull = digitalio.Pull.DOWN

btn_left_pin = digitalio.DigitalInOut(btn_left_pin)
btn_left_pin.direction = digitalio.Direction.INPUT
btn_left_pin.pull = digitalio.Pull.DOWN

btn_right_pin = digitalio.DigitalInOut(btn_right_pin)
btn_right_pin.direction = digitalio.Direction.INPUT
btn_right_pin.pull = digitalio.Pull.DOWN

btn_click_pin = digitalio.DigitalInOut(btn_click_pin)
btn_click_pin.direction = digitalio.Direction.INPUT
btn_click_pin.pull = digitalio.Pull.DOWN



while True:
    if btn_up_pin.value:
        keyboard.send(Keycode.UP_ARROW)
        while btn_up_pin.value:
            time.sleep(0.01)
    if btn_down_pin.value:
        keyboard.send(Keycode.DOWN_ARROW)
        while btn_down_pin.value:
            time.sleep(0.01)
    if btn_left_pin.value:
        keyboard.send(Keycode.LEFT_ARROW)
        while btn_left_pin.value:
            time.sleep(0.01)
    if btn_right_pin.value:
        keyboard.send(Keycode.RIGHT_ARROW)
        while btn_right_pin.value:
            time.sleep(0.01)
    if btn_click_pin.value:
        keyboard.send(Keycode.SPACE)
        while btn_click_pin.value:
            time.sleep(0.01)





