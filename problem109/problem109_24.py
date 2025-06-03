import numpy as np
n=int(input())
a=np.array([0]*4)
for i in range(n):
    s= str(input())
    if s=='AC':
        a[0]+=1
    elif s=='WA':
        a[1]+=1
    elif s=='TLE':
        a[2]+=1
    elif s=='RE':
        a[3]+=1
print('AC x '+str(a[0]))
print('WA x '+str(a[1]))
print('TLE x '+str(a[2]))
print('RE x '+str(a[3]))