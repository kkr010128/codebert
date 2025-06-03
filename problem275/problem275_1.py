prize = {1:300000,2:200000,3:100000}

a,b = [int(i) for i in input().split()]

if a == b == 1:
    print(1000000)
elif a < 4 and b < 4:
    print(prize[a] + prize[b])
elif a >= 4 and b < 4:
    print(prize[b])
elif b >= 4 and a < 4:
    print(prize[a])
else:
    print(0)
