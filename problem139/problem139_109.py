import sys
input = sys.stdin.readline

# A - Study Scheduling
h1, m1, h2, m2, k = map(int, input().split())

minute = (h2 - h1) * 60 + (m2 -m1)
print(minute - k)