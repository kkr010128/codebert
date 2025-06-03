h,k = map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
print(sum(arr[0:h-k]) if h>=k else 0)