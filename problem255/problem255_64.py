N = int(input())
S,T = input().split()
s = ''
for i in range(N):
    s += S[i]
    s+= T[i]
print(s)