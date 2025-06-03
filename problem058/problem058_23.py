c = 1
Answer = []

while c > 0:
    inp = input().split()
    n = int(inp[0])
    x = int(inp[1])
    c = n**2+x**2
    if c == 0:
        break

    flg = 0
    for i in range(1,min(int(x/3),n-1)):
        for j in range(i+1,min(int(x/2),n)):
            for k in range(j+1,n+1):
                if i+j+k == x:
                    flg += 1
    Answer.append(flg)

for l in range(0,len(Answer)):
    print(Answer[l])