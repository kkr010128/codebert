turn=int(input())
ten=[0,0]

for _ in range(turn):
    hikaku = input().split()
    if hikaku[0] < hikaku[1]:
        ten[1] +=3

    elif hikaku[0] > hikaku[1]:
        ten[0] +=3

    else:
        ten[0]+=1
        ten[1]+=1

print(" ".join(map(str,ten)))