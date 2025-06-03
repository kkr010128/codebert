import sys

 
H,W,K = list(map(int, input().split()))

c = []
for i in range(H):
    c.append(list(map(str, input().split()))[0])

o = 0
p = 0

for i in range(2**H):
    for j in range(2**W):
        o = 0
        for b,n in enumerate(bin(i)[2:].zfill(H)):
            for a,l in enumerate(bin(j)[2:].zfill(W)):
                if n == '0' and l == '0' and c[b][a]=='#':
                    o += 1
        if o == K:
            p += 1
print(p)
