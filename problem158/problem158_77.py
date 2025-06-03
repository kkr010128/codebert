K = int(input())
A, B = map(int, input().split())

x = 1000//K

for n in range(x+1):
    if (n * K >= A) and (n * K <= B):
        print('OK')
        break
    if n == x:
        print('NG')