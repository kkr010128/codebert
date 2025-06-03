S = input()
Slist = list(S)
big = ord('A')
small = ord('a')
diff = big-small
for i in range(len(Slist)):
    w = ord(Slist[i])
    if small <= w:
        #?°?????????????
        Slist[i] = chr(w+diff)
    elif big <= w:
        Slist[i] = chr(w-diff)
print(''.join(Slist))