n = int(input())
a = map(int,input().split(' '))
tallest = 0
step = 0
for i in a:
    if i < tallest:
        step = step + tallest - i
    else:
        tallest = i
print(step)