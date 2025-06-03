n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

print(sum(sorted(arr)[::-1][k:]))