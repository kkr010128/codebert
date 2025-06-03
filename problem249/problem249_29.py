import bisect

a, b, k = [int(i) for i in input().split()]

print(max(a-k,0), max(0,min(b,a+b-k)))