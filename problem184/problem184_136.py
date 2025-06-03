import sys
input = sys.stdin.readline
'''
n, m = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))
for test in range(int(input())):
'''
inf = 100000000000000000  # 1e17

s = input().strip()
if s[2] == s[3] and s[4] == s[5]:
    print("Yes")
else:
    print("No")
