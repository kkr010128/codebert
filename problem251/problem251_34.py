from collections import defaultdict
dic = defaultdict(int)
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
h = []

r, s, p = 0, 0, 0
for i in range(N):
    if i>=K:
        if T[i]==h[i-K]:
            h.append("x")
            continue
    
    if T[i]=="r":
        h.append("r")
        p+=1
    elif T[i]=="p":
        h.append("p")
        s+=1
    elif T[i]=="s":
        h.append("s")
        r+=1

print(p*P + r*R + s*S)