arr = [int(x) for x in input().split()]
print( max( max(arr[0]*arr[2], arr[0]*arr[3]), max(arr[1]*arr[2], arr[1]*arr[3]) ))