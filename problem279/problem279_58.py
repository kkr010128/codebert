N = int(input())
S = input()

if N%2!=0:
    print("No")
elif N%2 == 0:
    if S[0:N//2]==S[N//2:N+1]:
        print("Yes")
    else:
        print("No")