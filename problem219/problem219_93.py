# E - Payment

N = input().strip()

s = 0
carry = 0
five = False
for c in reversed(N):
    x = int(c) + carry
    if x == 5 and not five:
        s += x
        carry = 0
        five = True
    elif x >= 5:
        if five:
            x += 1
        s += 10 - x
        carry = 1
        five = False
    else:
        s += x
        carry = 0
        five = False
s += carry

print(s)
