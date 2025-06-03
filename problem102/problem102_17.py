n, k = [int(x) for x in input().strip().split()]
arr = [int(x) for x in input().strip().split()]


last = 0
for i in range(k):
    last += arr[i]

for i in range(k, len(arr)):
    curr = (last + arr[i]) - arr[i-k]
    if curr>last:
        print('Yes')
    else:
        print('No')
    last= curr
    
    
