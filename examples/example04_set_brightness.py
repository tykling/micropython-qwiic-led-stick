import time
from machine import I2C
from qwiic_led_stick.qwiic_led_stick import QwiicLedStick

i2c = I2C(1)
ledstick = QwiicLedStick(i2c)

reds = [255, 255, 170, 0, 0, 0, 0, 170, 255, 255]
greens = [0, 170, 255, 255, 255, 170, 0, 0, 0, 255]
blues = [0, 0, 0, 0, 170, 255, 255, 255, 170, 255]
ledstick.set_all_led_color(reds, greens, blues)
ledstick.set_all_led_same_brightness(16)
ledstick.set_led_brightness(10, 2)
time.sleep(1)

while True:
    for brightness in range(0,32):
        ledstick.set_all_led_same_brightness(brightness)
        time.sleep(1)
