a,v = map(int, input().split())
b,w = map(int, input().split())
t = int(input())
if v-w>0:
    if abs(a-b)/(v-w) <= t:
        print('YES')
        exit()
print('NO')

