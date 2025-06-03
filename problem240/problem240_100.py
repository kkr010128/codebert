#nは問題数　mは提出した回数　
n,m = map(int,input().split())
submit = []
check = [0] * n

for x in range(m):
    a,b = input().split()
    a = int(a)
    x = [a,b]
    submit.append(x)

o = 0
x = 0


for y in submit:
    if check[y[0]-1] == 0:
        if y[1] == "AC":
            o += 1
            check[y[0]-1] = 1
        elif y[1] == "WA":
            x += 1

for z in submit:
    if check[z[0]-1] == 0:
        if z[1] == "WA":
            x -= 1


print(o,x)
