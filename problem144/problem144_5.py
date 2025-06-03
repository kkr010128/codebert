import numpy as np

a, b, h, m = map(int, input().split())


def calc_rad(base, time):
    try:
        return 2 * np.pi * ((time) % base) / base
    except ZeroDivisionError:
        return 0


rad_a, rad_b = calc_rad(720, 60 * h + m), calc_rad(60, m)
ans = np.sqrt(a ** 2 + b ** 2 - 2 * a * b * np.cos(rad_a - rad_b))
print("{:.20f}".format(ans))