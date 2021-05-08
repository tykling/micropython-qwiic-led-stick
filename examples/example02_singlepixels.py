import time
from machine import I2C
from qwiic_led_stick.qwiic_led_stick import QwiicLedStick

i2c = I2C(1)
ledstick = QwiicLedStick(i2c)

while True:
    ledstick.turn_all_led_off()
    ledstick.set_led_color(4, 255, 0, 0)
    time.sleep(1)
    ledstick.turn_all_led_off()
    ledstick.set_led_color(6, 255, 0, 0)
    time.sleep(1)
