N = int(input())
if N%2 != 0:
    print("No")
    exit()
S=input()
N=N//2
if (S[:N]==S[-N:]):
    print("Yes")
else:
    print("No")