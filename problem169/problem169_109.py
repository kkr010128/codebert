def resolve():
    N = int(input())
    array = [0 for i in range(N)]
    buka = [int(i) for i in input().split()]

    for num in buka:
        array[num - 1] += 1
    for i in array:
        print(i)
resolve()