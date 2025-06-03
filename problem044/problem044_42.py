a,b,c = [int(x) for x in input().split( )]
div = []
for x in range(1,c+1):
    if c % x == 0:
        div.append(x)
r = []
for x in range(a,b+1):
    r.append(x)
answer = 0
for x in div:
    for y in r:
        if x == y:
            answer += 1
print(answer)
