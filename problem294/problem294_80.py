import bisect
N = int(input())

num_list = list(map(int,input().split()))
num_list.sort()
res = 0

for a in range(N-2):
    for b in range(a+1,N-1):
        k = bisect.bisect_left(num_list,num_list[a]+num_list[b])
        res += max(k-(b+1),0)
print(res)