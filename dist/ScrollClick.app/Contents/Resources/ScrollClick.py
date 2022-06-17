import pynput
import yaml
from pynput.mouse import Controller, Events, Button

mouse = Controller()

counter = 1

config = None

buttons = {'left': Button.left, 'right': Button.right}

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

def checkKey(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

if not checkKey(config, 'multiplier') and not checkKey(config, 'button'):
    config = {'multiplier': 1, 'button': 'right'}
if config['button'].lower() != 'right'.lower() and config['button'].lower() != 'left'.lower():
    config['button'] = Button.right
else:
    config['button'] = buttons[config['button'].lower()]

def on_scroll(x, y, dx, dy):
   mouse.click(config['button'], config['multiplier'])

def on_click(x, y, button, pressed):
    return

def darwin_intercept(event_type, event):
    import Quartz
    if event_type == 22:
        return None
    else:
        return event

if __name__ == '__main__':
    with pynput.mouse.Listener(darwin_intercept=darwin_intercept, on_scroll=on_scroll, on_click=on_click) as l:
        l.join()
    l.start()