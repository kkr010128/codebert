b=1
input()
for a in map(int,input().split()):b|=b<<a
input()
for m in map(int,input().split()):print(['no','yes'][(b>>m)&1])
