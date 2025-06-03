# first line > /dev/null
input()
items = sorted([int(i) for i in input().split(' ')])
print(items[0], items[-1], sum(items))