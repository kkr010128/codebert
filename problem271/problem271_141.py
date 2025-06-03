N = int(input())
S = input()
ans=""
for i in range(len(S)):
    ans += chr((ord(S[i])+N+13)%26+52+13)
print(ans)