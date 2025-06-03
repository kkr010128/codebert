k = int(input())
x = 7 % k
i = 1
set = set()
is_there = False

while not is_there:
    set.add(x)
    if x == 0:
        print(i)
        break
    x = (x*10+7) % k
    if x in set:
        is_there = True
    set.add(x)
    i += 1
    if x == 0:
        print(i)
        break
else:
    print('-1')