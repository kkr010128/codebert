k = int(input())

svn = 7
cnt = 1
for i in range(10**7):
    svn %= k
    if svn == 0:
        print(cnt)
        exit()
    svn *= 10
    svn += 7
    cnt += 1
print(-1)