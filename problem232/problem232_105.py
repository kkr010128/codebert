n, m = map(int, input().split())
if(n < m):
    for i in range (m):
        print(n, end = '')
else:
    for i in range (n):
        print(m, end = '')