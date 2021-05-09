import time
import urandom
from machine import I2C
from qwiic_led_stick.qwiic_led_stick import QwiicLedStick

i2c = I2C(1)
ledstick = QwiicLedStick(i2c)

while True:
    # count to 1024
    for i in range (0, 1024):
        # loop over LEDs in reverse
        for led in range(11,1):
            # is the bit for this LED a 0 or 1?
            if led & 1<<i:
                ledstick.set_led_color(led, 255, 0, 0, 0)
            else:
                ledstick.set_led_color(led, 0, 0, 0, 0)
        time.sleep(1)
