N = int(input())
S,T=input().split()
ST = "".join([S[i]+T[i] for i in range(N)])
print(ST)