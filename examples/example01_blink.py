import time
from machine import I2C
from qwiic_led_stick.qwiic_led_stick import QwiicLedStick

i2c = I2C(1)
ledstick = QwiicLedStick(i2c)
ledstick.set_all_led_same_color(50, 50, 50)

while True:
    ledstick.set_all_led_same_brightness(255)
    time.sleep(1)
    ledstick.turn_all_led_off()
    time.sleep(1)
