import bisect
import statistics
n = int(input())
a = list((int(x) for x in input().split()))

a.sort()
incl = []
score = 0

for i in range(len(a)):
    ain = a.pop()
    incl.append(ain)
    if i==0: continue
    if (len(incl)%2 == 1):
        score += incl[ int(len(incl)/2) ]
    else:
        # smaller of middle two
        score += incl[ int(len(incl)/2)-1 ]

print(score)