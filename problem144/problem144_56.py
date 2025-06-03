"""
○ 角速度 = θ / t [rad/s]
・時針
ω = θ / t
  = math.radians(360) / (12 * 60 * 60) [rad/s]
・分針
ω = θ / t
  = math.radians(360) / (60 * 60) [rad/s]
"""

import math

def colon():
    # 入力
    A, B, H, M = map(int, input().split())
    # 時針と分針の角速度
    angular_velocity_h = math.radians(360) / (12 * 60 * 60)
    angular_velocity_m = math.radians(360) / (60 * 60)
    # 0時を基準に時針が何度傾いたか
    radian_h = angular_velocity_h * ((H * 60 * 60) + (M * 60))
    # 0時を基準に分針が何度傾いたか
    radian_m = angular_velocity_m * (M * 60)
    # 時針と分針の間の角度
    radian_hm = abs(radian_h - radian_m)
    if radian_hm > math.pi:
        radian_hm = 2 * math.pi - radian_hm
    elif radian_hm == math.pi:
        return A + B
    elif math.pi > radian_hm:
        pass
    # 端点の距離
    distance = math.sqrt((A**2 + B**2) - (2 * A * B * math.cos(radian_hm)))
    # 戻り値
    return distance

result = colon()
print(result)