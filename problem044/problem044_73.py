a,b,c = map(int,raw_input().split())
i = 0
for x in range(a,b+1):
    if c % x==0:
        i += 1
if a == b:
    if c % a == 0:
        i = 1

print i