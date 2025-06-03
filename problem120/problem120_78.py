k = int(input().split(' ')[1])
print(sum( sorted([int(n) for n in input().split(' ')])[0:k]))