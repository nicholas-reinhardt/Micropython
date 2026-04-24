from machine import ADC, Pin
import time

# Set up ADC on GPIO3
adc = ADC(Pin(0))

# Optionally configure attenuation
adc.atten(ADC.ATTN_11DB)  # Allows up to ~3.6V (not always needed or supported)

# Optionally set resolution (may not affect ESP32-C3)
# adc.width(ADC.WIDTH_12BIT)  # ESP32 typically defaults to 12-bit

# Read and print raw ADC values
while True:
    raw = adc.read()
    print("Raw ADC:", raw)
    time.sleep(0.5)
