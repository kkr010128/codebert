residence = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
n = int(input())
sep = "#"*20
s = ""
for i in range(n):
    b,f,r,v = map(int,input().split())
    residence[b-1][f-1][r-1] += v

for i in residence:
    for j in i:
        s += " "+" ".join(map(str,j)) + "\n"

    s += sep+"\n"

print(s.rstrip(sep+"\n"))