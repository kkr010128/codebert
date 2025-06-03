#!usr/bin/env python3

def string_five_numbers_spliter():
    """Split a given space-separated five numbers in a string into integers

    Return five integer values from a given space-separated five integers in a string.

    Returns:
        Five integer values; namely, w, h, x, y and r
    """
    w, h, x, y, r = [int(i) for i in input().split()]
    return w, h, x, y, r


def main():
    # Given that there are a rectangle and a circle.
    # Let w, h, x, y and r be such that:
    # w = width of the rectangle
    # h = height of thek rectangle
    # x = x coordinate for the centre of the circle
    # y = y coordinate for the centre of the circle
    # r = diameter of the circle
    w, h, x, y, r = string_five_numbers_spliter()

    if (not (x < 0) and not (y < 0) and
        not (x + r < 0) and not (y + r < 0) and
        not (x + r > w) and not (y + r > h)):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()