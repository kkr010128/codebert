
import math
N, X, T = [int(x) for x in input().split(" ")]
times = math.ceil(N/X)
print(times * T)