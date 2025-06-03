l = []
while True:
    value = int(raw_input())
    if value == 0:
        break
    else:
        l.append(value)

for i, v in enumerate(l, 1):
    print("Case %d: %d") % (i, v)