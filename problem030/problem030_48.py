import math

len_a, len_b, deg_C = map(int,input().split(" "))
rad_C = math.radians(deg_C)

#area
S = (1/2) * len_a * len_b * math.sin(rad_C)
#Length
L = len_a + len_b + math.sqrt(len_a ** 2 + len_b ** 2 - 2 * len_a * len_b * math.cos(rad_C))
#height
h = len_b * math.sin(rad_C)

print("{:.5f}\n{:.5f}\n{:.5f}".format(S,L,h))