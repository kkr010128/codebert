N = int(input())
S = input()

base = ord("A")

ans = ""

for i in range(len(S)):
    p = (ord(S[i])-base)
    
    s = (p+N) % 26
    
    ans += chr(s+base)

print(ans)