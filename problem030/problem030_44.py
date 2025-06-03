#!/usr/bin/env python3

import math
import sys


def calculate_area(side_a, side_b, angle_c):
    return (side_a*side_b*math.sin(math.radians(angle_c))) / 2


def calculate_perimeter(side_a, side_b, angle_c):
    side_c = math.sqrt(side_a**2 + side_b**2
                       - 2*side_a*side_b*math.cos(math.radians(angle_c)))
    return side_a + side_b + side_c


def calculate_height_from_side_a(side_a, area):
    return (area*2)/side_a


def main():
    nums = [float(num) for num in sys.stdin.readline().split()]

    area = calculate_area(nums[0], nums[1], nums[2])
    perimeter = calculate_perimeter(nums[0], nums[1], nums[2])
    height_from_side_a = calculate_height_from_side_a(nums[0], area)

    print(area)
    print(perimeter)
    print(height_from_side_a)


if __name__ == '__main__':
    main()