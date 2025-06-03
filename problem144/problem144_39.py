a, b, h, m = map(int, input().split())
import math

s = abs(360*((h/12)+(m/720)) - 360*(m/60))
print(math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(s))))
