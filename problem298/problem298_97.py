n, k = map(int, input().split())
lst = [int(i) for i in input().split()]
print(len([j for j in lst if j >= k]))
