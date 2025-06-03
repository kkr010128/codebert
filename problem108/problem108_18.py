import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())

num = (N + 1000 - 1 )// 1000

print(num * 1000 - N)