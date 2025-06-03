import math
#入力
x = int(input())
x_upper = (x+1) / 1.08
x_lower = x / 1.08
x_candidate = math.ceil(x_lower)
if x_lower <= x_candidate < x_upper:
    print(x_candidate)
else:
    print(":(")