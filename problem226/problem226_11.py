h,n = map(int,input().split())
arr=list(map(int,input().split()))
print("No" if h>sum(arr) else "Yes")