a = []
while True:
    arr = map(int,raw_input().split())
    if arr[0] == 0 and arr[1] == 0:
        break
    arr.sort()
    arr = map(str,arr)
    print ' '.join(arr)