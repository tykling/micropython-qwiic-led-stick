import time
import urandom
from machine import I2C
from qwiic_led_stick.qwiic_led_stick import QwiicLedStick

i2c = I2C(1)
ledstick = QwiicLedStick(i2c)

while True:
    reds = [urandom.getrandbits(8) for _ in range(0,10)]
    greens = [urandom.getrandbits(8) for _ in range(0,10)]
    blues = [urandom.getrandbits(8) for _ in range(0,10)]
    brightnesses = [urandom.getrandbits(5) for _ in range(0,10)]
    ledstick.set_all_led_color(reds, greens, blues)
    for led in range(1,11):
        ledstick.set_led_brightness(led, brightnesses[led])
    time.sleep(1)
