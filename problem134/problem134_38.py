from sys import exit

n = int(input())
num_list = [int(i) for i in input().split()]
if 0 in num_list:
    print(0)
    exit()
ans = 1
for i in range(n):
    ans *= num_list[i]
    if ans > 10**18:
        print(-1)
        exit()
print(ans)