import time
import machine
import neopixel


# Setup
wdt = machine.WDT(timeout=5000)  # Watchdog timer 5s
n = 1    # Number of LEDs
np = neopixel.NeoPixel(machine.Pin(8), n)
button = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)


# Functions-----------------

# Startup sequence
def startup():
    np[0] = (1, 0, 0)
    np.write()
    time.sleep_ms(500)
    np[0] = (0, 1, 0)
    np.write()
    time.sleep_ms(500)
    np[0] = (0, 0, 1)
    np.write()
    time.sleep_ms(500)
    wdt.feed()  # Reset watchdog timer


# button press turns on light
def press():
    while True:
        wdt.feed()  # Reset watchdog timer

        if button.value() == 0:  # Button is pressed
            np[0] = (1, 1, 1)  # ON
        else:
            np[0] = (0, 0, 0)  # OFF
        np.write()
        time.sleep_ms(20)  # Debounce delay


# Actions-----------------

# run startup sequence
startup()

# run button press function
press()

