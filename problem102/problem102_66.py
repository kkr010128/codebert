n, k = map(int, input().split())
data = list(map(int, input().split()))

left = 0
right = k
while right < n:
    if data[left] < data[right]:
        print('Yes')
    else:
        print('No')
    left += 1
    right += 1
