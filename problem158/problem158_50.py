import math
K = int(input())
A, B = map(int, input().split())
largest = math.floor(B/K)*K
print("OK") if largest >= A else print("NG")