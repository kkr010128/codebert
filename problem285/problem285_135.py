s = str(input())
#s = "<>>><<><<<<<>>><"
ans = 0
def leftmore(ln):
    ret = [0]
    cur = 0
    for c in ln:
        if c == "<":
            cur += 1
        else:
            cur = 0
        
        ret.append(cur)
    return ret

def rightless(ln):
    revl = reversed(ln)
    ret = [0]
    cur = 0
    for c in revl:
        if c == ">":
            cur += 1
        else:
            cur = 0
        ret.append(cur)
    return list(reversed(ret))

lm = leftmore(s)
rl = rightless(s)
for i in range(len(s)+1):
    ans += max(lm[i],rl[i])
print(ans)