import keyboard

win_enabled = False
win_handler = None
def win_toggle():
    global win_enabled
    win_enabled = not win_enabled
    if win_enabled: win_disable()
    else: win_enable()

def win_callback(_var):
    if keyboard.is_pressed('alt'):
        win_toggle()

def win_disable():
    global win_handler
    win_handler = keyboard.hook_key("windows", win_callback, suppress=True)
    print("Win Key Disabled")

def win_enable():
    global running
    keyboard.unhook(win_handler)
    print("Win Key Enabled")

keyboard.add_hotkey("alt+windows", win_toggle, args=("", ))
keyboard.wait()