n = int(input())
array = list(map(int, input().split()))

total = 0
for i in range(n):
    total += array[i] 
array.sort()

print(array[0], array[-1], total)