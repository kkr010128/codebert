N = int(input())
S = input().rstrip()
if S[N//2:] == S[:N//2]:
    print("Yes")
else:
    print("No")