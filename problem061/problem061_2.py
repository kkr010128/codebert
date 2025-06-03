i = map(str, raw_input())

def check(x):
    if x.islower():
        return x.upper()
    return x.lower()

print ''.join(map(check, i))