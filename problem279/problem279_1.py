N = int(input())
S = input()
n = N/2
if S == S[int(n):] * 2:
    print("Yes")
else:
    print("No")