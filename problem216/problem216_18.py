import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

a,b,c = map(int, input().split())

if a == b and a != c and b != c:
    print("Yes")
elif a == c and a != b and c != b:
    print("Yes")
elif b == c and a != b and a != c:
    print("Yes")
else:
    print("No")
