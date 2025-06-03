N = int(input())
A = list(map(int,input().split()))
num_b = 0
cnt = 0
for i in A:
    if num_b > i:
        cnt += num_b - i
    else:
        num_b = i
print(cnt)