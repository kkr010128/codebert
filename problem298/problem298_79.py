n, k = list(map(int, input().split(' ')))
print(sum([tall >= k for tall in list(map(int, input().split(' ')))]))