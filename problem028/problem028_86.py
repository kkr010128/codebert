n, m = map(int, input().split())
c_list = list(map(int, input().split()))
c_list.sort()
dp_list = [0] + [10**9]*(n)
for i in range(1, n+1):
    for c in c_list:
        if i - c >= 0:
            dp_list[i] = min(dp_list[i], dp_list[i-c]+1)
        else:
            break
print(dp_list[-1])

