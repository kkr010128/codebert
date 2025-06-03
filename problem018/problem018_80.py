stak = []
for i in input().split():
    if i in "+-*":
        a = stak.pop()
        b = stak.pop()
        stak.append(str(eval(b + i + a)))
    else:
        stak.append(i)
print(stak.pop())
