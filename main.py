import keyboard, time

win_enabled = False
win_handler = None
win_timestamp = 0

def win_toggle(_str):
    global win_enabled
    win_enabled = not win_enabled
    if win_enabled: win_disable()
    else: win_enable()

def win_callback(_var):
    global win_timestamp
    if keyboard.is_pressed('alt') and time.time() - win_timestamp >= 0.1:
        win_toggle("")

def win_disable():
    global win_handler, win_timestamp
    win_timestamp = time.time()
    win_handler = keyboard.hook_key("windows", win_callback, suppress=True)
    if keyboard.is_pressed('windows'):
        keyboard.release("windows")
    
    print("Win Key Disabled")

def win_enable():
    global running
    keyboard.unhook(win_handler)
    print("Win Key Enabled")

keyboard.add_hotkey("alt+windows", win_toggle, args=("", ))
keyboard.wait()