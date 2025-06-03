def insertion_sort(arr):
    print(" ".join(map(str, arr)))
    for i in range(1,len(arr)):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        print(" ".join(map(str, arr)))

input()
arr = list(map(int, input().split()))
insertion_sort(arr)
