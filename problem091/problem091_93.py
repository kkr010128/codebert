n = int(input())
ls = sorted(list(map(int, input().split())))
cnt = 0
for i in range(len(ls) - 2):
    a = ls[i]
    for j in range(i+1, len(ls) - 1):
        b = ls[j]
        for k in range(j+1, len(ls)):
            c = ls[k]
            if a==b or a==c or b==c:
                continue
            if a+b > c and b+c > a and c+a > b:
                cnt += 1
print(cnt)