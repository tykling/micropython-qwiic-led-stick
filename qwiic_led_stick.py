# I2C registers for controlling Qwiic LED Stick
I2C_REGISTER_CHANGE_ADDRESS = 0xC7
I2C_REGISTER_CHANGE_LED_LENGTH = 0x70
I2C_REGISTER_WRITE_SINGLE_LED_COLOR = 0x71
I2C_REGISTER_WRITE_ALL_LED_COLOR = 0x72
I2C_REGISTER_WRITE_RED_ARRAY = 0x73
I2C_REGISTER_WRITE_GREEN_ARRAY = 0x74
I2C_REGISTER_WRITE_BLUE_ARRAY = 0x75
I2C_REGISTER_WRITE_SINGLE_LED_BRIGHTNESS = 0x76
I2C_REGISTER_WRITE_ALL_LED_BRIGHTNESS = 0x77
I2C_REGISTER_WRITE_ALL_LED_OFF = 0x78

class QwiicLedStick:
    def __init__(self, i2c, address=0x23):
        """Use the provided I2C bus and default to address 0x23."""
        self.i2c = i2c
        self.address = address


    def write(self, register, payload):
        """Convenience method to write a payload to an I2C register."""
        self.i2c.writeto_mem(self.address, register, payload)


    def set_led_color(self, led, red, green, blue):
        """Change the color of one specific LED."""
        led = min(max(led, 1), 10)
        red = min(max(red, 0), 255)
        green = min(max(green, 0), 255)
        blue = min(max(blue, 0), 255)
        self.write(register=I2C_REGISTER_WRITE_SINGLE_LED_COLOR, payload=bytearray([led, red, green, blue]))


    def set_all_led_color(self, reds, greens, blues):
        """Set the color of all LEDs from three lists of colors."""
        self.write(register=I2C_REGISTER_WRITE_RED_ARRAY, payload=bytearray(reds))
        self.write(register=I2C_REGISTER_WRITE_GREEN_ARRAY, payload=bytearray(greens))
        self.write(register=I2C_REGISTER_WRITE_BLUE_ARRAY, payload=bytearray(blues))


    def set_led_brightness(self, led, brightness):
        """Change the brightness of a specific LED, while keeping the current color.

        Brightness must be a value between 0-31. To turn LEDs off but remember their
        previous color, set brightness to 0
        """
        led = min(max(led, 1), 10)
        brightness = min(max(brightness, 0), 31)
        self.write(register=I2C_REGISTER_WRITE_SINGLE_LED_BRIGHTNESS, payload=bytearray([led, brightness]))


    def set_all_led_same_color(self, red, green, blue):
        """Change the color of all LEDs to the same color."""
        for led in range(1,11):
            self.set_led_color(led, red, green, blue)


    def set_all_led_same_brightness(self, brightness):
        """Change the brightness of all LEDs to the same brightness."""
        brightness = min(max(brightness, 0), 31)
        for led in range(1,11):
            self.set_led_brightness(led, brightness)


    def turn_all_led_off(self):
        """Turn all LEDs off (but keep their current colors)."""
        self.set_all_led_same_brightness(0)
