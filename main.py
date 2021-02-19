from machine import Pin, Timer

# Define the onboard led as variable.
ONBOARD_LED = 25

# Set the Pin to an output.
onboard_led = Pin(ONBOARD_LED, Pin.OUT)
# Initialize a timer to turn on and off the led.
intervall = Timer()

# Function to do the toggle magic. Has to take an argument, otherwise a TypeError will be thrown, but
# works without argument as well.
def blink(timer):
    onboard_led.toggle()

if __name__ == '__main__':
    # Set the intervall for toggling.
    intervall.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)