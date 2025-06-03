i = map(str, raw_input())

def check(x):
    if x.islower():
        return x.upper()
    else:
        return x.lower()

ret = []
for x in i:
    ret += [check(x)]

print ''.join(ret)