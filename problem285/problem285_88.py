s = input()
inc = 0
dec = 0
increasing = True
ans = 0
for c in s:
    if increasing:
        if c == '<':
            inc += 1
        else:
            increasing = False
            dec += 1
    else:
        if  c == '>':
            dec += 1
        else:
            if inc > dec:
                inc, dec = dec, inc
            ans += inc * (inc - 1) // 2 + dec * (dec + 1) // 2
            increasing = True
            inc = 1
            dec = 0
else:
    if increasing:
        ans += inc * (inc + 1) // 2
    else:
        if inc > dec:
            inc, dec = dec, inc
        ans += inc * (inc - 1) // 2 + dec * (dec + 1) // 2
print(ans) 
