# ex 2.3.4

class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x       # x coordinate
        self._y = y       # y coordinate
        self._red = red     # a value between 0 and 255    0 - dark pixel, 255 - bright pixel
        self._green = green   # a value between 0 and 255
        self._blue = blue    # a value between 0 and 255

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) / 3
        self._red = round(avg)
        self._green = round(avg)
        self._blue = round(avg)

    def print_pixel_info(self):
        if not(self._red and self._green) and self._blue > 50:
            print("X:", self._x, "\tY:", self._y, "\tColor:({}, {}, {})".format(self._red, self._green, self._blue),
                  "\tBlue")
        elif not(self._red and self._blue) and self._green > 50:
            print("X:", self._x, "Y:", self._y, "\tColor:({}, {}, {})".format(self._red, self._green, self._blue),
                  "\tGreen")
        elif not(self._green and self._blue) and self._red > 50:
            print("X:", self._x, "\tY:", self._y, "\tColor:({}, {}, {})".format(self._red, self._green, self._blue),
                  "\tRed")
        else:
            print("X:", self._x, "\tY:", self._y, "\tColor:({}, {}, {})".format(self._red, self._green, self._blue))


def main():
    pixel1 = Pixel(5, 6, 250)
    pixel1.print_pixel_info()
    pixel1.set_grayscale()
    pixel1.print_pixel_info()


if __name__ == "__main__":
    main()