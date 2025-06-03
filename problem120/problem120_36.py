total,amount=[int(x) for x in input().split()]
array=sorted([int(x) for x in input().split()])
print(sum(array[0:amount]))