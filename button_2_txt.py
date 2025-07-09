from machine import Pin
import time

boot_button = Pin(9, Pin.IN, Pin.PULL_UP)

print("Waiting for button press...")

while True:
    if not boot_button.value():
        with open("log.txt", "a") as f:
            f.write("I pushed the button\n")
        print("Logged to file")
        time.sleep(0.3)  # debounce delay
