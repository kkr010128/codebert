# 165 A
K = int(input())
A,B = list(map(int, input().split()))
m = B%K
print('OK') if B-m >= A else print('NG')