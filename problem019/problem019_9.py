from collections import OrderedDict

n, q = map(int, input().split())
od = OrderedDict()

for i in range(n):
    name, time = input().split()
    od.update({name: int(time)})
total = 0

while len(od) > 0:
    name, time = od.popitem(False)
    if time <= q:
        total += time
        print("{} {}".format(name, total))
    else:
        total += q
        time -= q
        od.update({name: time})