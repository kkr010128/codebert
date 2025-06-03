import math

a, b , n = map(int, input().split())

ans1 = (a*(b-1))//b
ans2 = (a*n)//b

print(min(ans1, ans2))