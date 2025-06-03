import math
member = []
score = []
while True:
    num = int(raw_input())
    if num == 0: break
    member.append(num)
    score.append(map(int, raw_input().split()))

alpha = []
for m, s in zip(member, score):
    average = sum(s)/float(m)
    sigma = 0
    for t in s:
        sigma += (t - average)**2
    else:
        alpha += [sigma/m]

for a in alpha:
    #print '%.8f' % math.sqrt(a)
    print math.sqrt(a)