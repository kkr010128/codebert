import math
a, b, h, m = map(int, input().split())
m_h = m
if h ==0:
    h = 12
if m == 0:
    m_h = 0
    m = 60
sub_degrees = abs((360/12) * h + (30/12) * (m_h/5)  - (360/60) * m )
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(sub_degrees))))