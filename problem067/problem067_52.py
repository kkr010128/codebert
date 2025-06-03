n = int(input())
p1 = p2 = 0
for _ in range(n):
    taro,hanako = map(str,input().split(" "))
    if taro>hanako: p1 += 3
    elif taro<hanako: p2 += 3
    else:
        p1 += 1
        p2 += 1
print(p1,p2)

