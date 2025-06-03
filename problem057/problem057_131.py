def judge(m,f,r):
    ret = 'F'
    score = m + f
    if -1 in (m,f): pass
    elif score >= 80: ret = 'A'
    elif score >= 65: ret = 'B'
    elif score >= 50: ret = 'C'
    elif score >= 30: 
        ret = 'D'
        if r >= 50:ret = 'C'
    return ret     
while True:
    m,f,r=map(int,input().split())
    if m==f==r==-1: break
    print(judge(m,f,r))