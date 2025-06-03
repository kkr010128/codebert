N, X, T = map(int, input().split())
import math
number_of_times = math.ceil(N/X)
total_time = T * number_of_times
print(total_time)
