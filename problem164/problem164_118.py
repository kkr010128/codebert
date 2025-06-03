thp, tak, ahp, aak = map(int, input().split())
judge = 0
while thp > 0 and ahp > 0:
    if judge == 0:
        ahp -= tak
        judge = 1
    else:
        thp -= aak
        judge = 0
if thp <= 0:
    print("No")
else:
    print("Yes")