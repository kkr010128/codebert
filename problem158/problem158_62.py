K = int(input())
A,B = map(int, input().split())
target = 0
target = B - B % K
if A <= target:
    print('OK')
else:
    print('NG')