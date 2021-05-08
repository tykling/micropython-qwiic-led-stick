# Pixel color order constants
RGB = (0, 1, 2)
RBG = (0, 2, 1)
GRB = (1, 0, 2)
GBR = (1, 2, 0)
BRG = (2, 0, 1)
BGR = (2, 1, 0)

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
        self.i2c = i2c
        self.address = address

    def write(self, register, payload):
        self.i2c.writeto_mem(self.address, register, payload)

    def set_led_color(self, led, red, green, blue):
        """Change the color of one specific LED."""
        led = min(max(led, 1), 10)
        red = min(max(red, 0), 255)
        green = min(max(green, 0), 255)
        blue = min(max(blue, 0), 255)
        self.write(register=I2C_REGISTER_WRITE_SINGLE_LED_COLOR, payload=bytearray([led, red, green, blue]))

    def set_led_brightness(self, led, brightness):
        """Change the brightness of a specific LED, while keeping the current color.

        Brightness must be a value between 0-31. To turn LEDs off but remember their
        previous color, set brightness to 0
        """
        led = min(max(led, 1), 10)
        brightness = min(max(brightness, 0), 31)
        self.write(register=I2C_REGISTER_WRITE_SINGLE_LED_BRIGHTNESS, payload=bytearray([led, brightness]))

    def set_all_led_color(self, red, green, blue):
        """Change the color of all LEDs."""
        red = min(max(red, 0), 255)
        green = min(max(green, 0), 255)
        blue = min(max(blue, 0), 255)
        for led in range(0,10):
            self.set_led_color(led, red, green, blue)

