n = int(input())
arr = list(map(int, input().split()))

answer = 0
for idx1 in range(0, len(arr) - 2):
    for idx2 in range(idx1+1, len(arr) - 1):
        for idx3 in range(idx2+1, len(arr)):
            if arr[idx1] == arr[idx2] or arr[idx1] == arr[idx3] or arr[idx2] == arr[idx3]:
                continue
            if arr[idx1] + arr[idx2] > arr[idx3] and arr[idx1] + arr[idx3] > arr[idx2] and arr[idx2] + arr[idx3] > arr[idx1]:
                answer += 1

print(answer)