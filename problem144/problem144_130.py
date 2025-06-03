import math
A, B, H, M = map(int, input().split())

SP_HOUR =  360 / (12 * 60)
SP_MIN = 360 / 60

angle = (H * 60 + M) * SP_HOUR - M * SP_MIN
if angle < 0:
    angle += 360

# print(math.cos(0))
# print(math.cos(3.14))
# print("angle", angle)
# print("angle in radian", math.radians(angle))
#Law of cosines
ans_squ = A * A + B * B - 2 * A * B * math.cos(math.radians(angle))

print(math.sqrt(ans_squ))
