import math


def main(a, b, h, m):
    # 短針の座標を取得
    rad1 = 2 * math.pi * (h + m / 60.0) / 12.0
    x1 = a * math.cos(rad1)
    y1 = a * math.sin(rad1)

    # 長針の座標を計算
    rad2 = 2 * math.pi * m / 60.0
    x2 = b * math.cos(rad2)
    y2 = b * math.sin(rad2)

    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(d)


if __name__ == "__main__":
    a, b, h, m = map(int,input().split())
    main(a, b, h, m)
