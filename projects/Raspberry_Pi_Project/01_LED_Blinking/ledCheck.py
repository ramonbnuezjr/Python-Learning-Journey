# Importing the necessary libraries
from gpiozero import LED
from time import sleep

# Assigning the GPIO pin 18 to the LED
led = LED(18) 

while True:
    led.on() # Turn on the LED
    sleep(1) # Wait for 1 second
    led.off() # Turn off the LED
    sleep(1) # Wait for 1 second