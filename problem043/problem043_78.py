from sys import stdin

while True:
    arr = [int(n) for n in stdin.readline().rstrip().split()]

    if arr[0] == arr[1] == 0:
        break

    arr.sort()
    print(arr[0], arr[1])

