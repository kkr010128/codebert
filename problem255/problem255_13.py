n=input()
s,t=input().split()

pt = (p + t for p, t in zip(s, t))
print(''.join(pt))