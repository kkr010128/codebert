count = int(input())
array = [int(i) for i in input().split(" ")]

for n in range( count - 1, 0, -1):
    print(array[n], end = " ")
print(array[0])    