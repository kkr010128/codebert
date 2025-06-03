x = {"S": list(range(1, 14)), "H": list(range(1, 14)),
     "C": list(range(1, 14)), "D": list(range(1, 14))}
n = int(input())
for i in range(n):
    tmp = input().split()
    key = tmp[0]
    num = int(tmp[1])
    x[key].remove(num)

keys = ["S", "H", "C", "D"]
for key in keys:
    if len(x[key])==0:
        pass
    else:
        for i in x[key]:
            print(key, i)