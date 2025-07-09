from machine import Pin
import time

# Boot button is usually GPIO9 on the ESP32-C3
boot_button = Pin(9, Pin.IN, Pin.PULL_UP)

print("Waiting for button press...")

while True:
    if not boot_button.value():  # Button is pressed when LOW
        print("I pushed the button")
        time.sleep(0.3)  # debounce delay
