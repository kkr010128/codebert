n, m = map(int, input().split())
num = [None] * n
a = [tuple(map(int, input().split())) for _ in range(m)]
for pos, val in a:
    if num[pos - 1] != None and num[pos - 1] != val:
        print(-1)
        exit()
    num[pos - 1] = val
if n == 1 and num[0] == None:
    num[0] = 0
canBeZero = False
for i in range(n):
    if num[i] == None:
        num[i] = 0 if canBeZero else 1
    if num[i]:
        canBeZero = True
ret = str(int(''.join(map(str, num))))
print(ret if len(ret) == n else -1)