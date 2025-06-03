n,m = map(int,input().split())
s = input()
s = s[::-1]

tmp = 0
sum1 = 0
ans = []

while tmp < n:
    for i in range(m, 0, -1):
        flag = False
        if tmp + i <= n:
            if s[tmp+i] == '0':
                tmp += i
                flag = True
                sum1 += 1
                ans.append(i)
                break
    if not flag:
        print(-1)
        exit()

for i in ans[::-1]:
    print(i, end = ' ')
