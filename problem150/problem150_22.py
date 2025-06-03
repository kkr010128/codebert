n, k = map(int, input().split())
a = list(map(int, input().split()))

num = 1
li = [1]
flag = [True] * n
flag[0] = False

for i in range(k):
    num = a[num-1]
    if flag[num-1]:
        li.append(num)
        flag[num-1] = False
    else:
        break

d = li.index(num)
ans = (k-d)%(len(li)-d)+d

print(li[ans])