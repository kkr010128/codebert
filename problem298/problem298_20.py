n,k=[int(x) for x in input().split()]
d=[int(x) for x in input().split()]

t=[x for x in d if x>=k]

print(len(t))