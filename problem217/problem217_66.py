N=int(input())
S=[int(s) for s in input().split()]
for i in range(N):
    if S[i]%2==0 and S[i]%5!=0 and S[i]%3!=0:
        print("DENIED")
        break
    elif i==N-1:
        print("APPROVED")