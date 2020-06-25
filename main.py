"""
ttgo_hello.py

    Writes "Hello!" in random colors at random locations on a
    LILYGO® TTGO T-Display.

    https://www.youtube.com/watch?v=atBa0BYPAAc

"""
import random
from machine import Pin, SPI
import st7789py as st7789

# Choose a font

# from fonts import vga1_8x8 as font
# from fonts import vga2_8x8 as font
# from fonts import vga1_8x16 as font
# from fonts import vga2_8x16 as font
# from fonts import vga1_16x16 as font
# from fonts import vga1_bold_16x16 as font
# from fonts import vga2_16x16 as font
# from fonts import vga2_bold_16x16 as font
# from fonts import vga1_16x32 as font
# from fonts import vga1_bold_16x32 as font
# from fonts import vga2_16x32 as font
import vga2_bold_16x32 as font

def main():
    # ESP 8266 SCK D5, MOSI D7
    # ESP32 SCK
    spi = SPI(1, 10000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
    tft = st7789.ST7789(spi, 240, 240, reset=Pin(27, Pin.OUT), dc=Pin(26, Pin.OUT), backlight=Pin(25, Pin.OUT), rotation=0)

    """
    tft = st7789.ST7789(spi, 240, 240,
        # D0, 16
        reset=Pin(27, Pin.OUT),
        # D4. Though NA for my board. Assign to D4 to make program happy. Don't connect.
        cs=Pin(2, Pin.OUT),
        # D1, 5
        dc=Pin(26, Pin.OUT),
        # D2, 4
        backlight=Pin(25, Pin.OUT),
        rotation=0) """

    tft.fill(0)
    tft.line(0, 0, 100, 100, st7789.color565(200, 0, 0))

"""
    while True:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(0)
            col_max = tft.width - font.WIDTH*6
            row_max = tft.height - font.HEIGHT

            for _ in range(100):
                tft.text(
                    font,
                    "Hello!",
                    random.randint(0, col_max),
                    random.randint(0, row_max),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)),
                    st7789.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8))
                )
"""

main()