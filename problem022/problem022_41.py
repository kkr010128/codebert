def linearSearch(key, list, N):
    l = list + [key]
    i = 0
    while l[i] != key:
        i += 1
    return int(i != N)


N1 = int(input())
arr1 = [int(n) for n in input().split()]
N2 = int(input())
arr2 = [int(n) for n in input().split()]

print(sum([linearSearch(key, arr1, N1) for key in arr2]))

