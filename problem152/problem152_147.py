N = int(input())
S_s = [input() for _ in range(N)]
S_data1 = []
S_data2 = []
for S in S_s:
    life = 0
    A=0
    for c in S:
        if c == '(':
            life += 1
        else:
            if life > 0:
                life -= 1
            else:
                A += 1
    if(A<life):
        S_data1.append(tuple([A,life]))
    else:
        S_data2.append(tuple([A,life]))
S_data1.sort()
S_data2 = sorted(S_data2, key=lambda x:-x[1])
S_data1.extend(S_data2)
S_data = tuple(S_data1)
life = 0
answer = True
for S_datum in S_data:
    life -= S_datum[0]
    if life < 0:
        answer = False
        break
    life += S_datum[1]
else:
    if life != 0:
        answer = False

if answer:
    print("Yes")
else:
    print("No")