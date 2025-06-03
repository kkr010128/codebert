n = int(input())
s = input()

def rot(c, r):
    base = 65
    return chr((ord(c)-base+r)%26+base)

print(''.join([rot(i, n) for i in s]))
