import keyboard, time

win_enabled = False
win_handler = None
alt_handler = None
win_toggled = False
win_timestamp = 0

def win_toggle(_str):
    global win_enabled
    if not win_toggled:
        win_enabled = not win_enabled
        if win_enabled: win_disable()
        else: win_enable()

def win_callback(_var):
    global win_timestamp, win_toggled
    if keyboard.is_pressed('alt'):
        win_toggle("")

def alt_release(_str):
    global win_toggled
    win_toggled = False
    keyboard.unhook(alt_handler)

def win_disable():
    global win_handler, alt_handler, win_timestamp, win_toggled

    win_toggled = True
    win_timestamp = time.time()
    win_handler = keyboard.hook_key("windows", win_callback, suppress=True)
    alt_handler = keyboard.on_release_key("alt", alt_release, suppress=False)

    if keyboard.is_pressed('windows'):
        keyboard.release("windows")
    
    print("Win Key Disabled")

def win_enable():
    global running, win_toggled, alt_handler
    win_toggled = True
    keyboard.unhook(win_handler)
    alt_handler = keyboard.on_release_key("alt", alt_release, suppress=False)
    print("Win Key Enabled")

keyboard.add_hotkey("alt+windows", win_toggle, args=("", ))

try:
    keyboard.wait()
except KeyboardInterrupt:
    pass