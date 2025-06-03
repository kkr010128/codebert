n = int(input())
l = list(map(int, input().split()))
array = [0] * n
for i in l:
    array[i-1] += 1
for i in array:
    print(i)