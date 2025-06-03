import math
a = float(input())
print(str("{0:.6f}".format((a * a) * math.pi)) + " " + str("{0:.5f}".format((a + a) * math.pi)))
