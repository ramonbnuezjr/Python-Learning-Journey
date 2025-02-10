# Import the necessary modules:
from gpiozero import PWMLED  # PWMLED allows brightness control using PWM.
from time import sleep       # sleep lets us add delays for a smooth fade.

# Initialize the LED on GPIO 18:
led = PWMLED(18)

def fade_led():
    # Fade In: Gradually increase brightness from 0 (off) to 1 (full brightness)
    for brightness in range(0, 101):  # 0 to 100 inclusive.
        led.value = brightness / 100  # Scale to 0.0-1.0 range.
        sleep(0.01)  # Wait 10 milliseconds.
    
    # Fade Out: Gradually decrease brightness from 1 back to 0.
    for brightness in range(100, -1, -1):
        led.value = brightness / 100
        sleep(0.01)

# Main loop: Keep running the fade effect
while True:
    fade_led()