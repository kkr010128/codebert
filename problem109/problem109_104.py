N=int(input())
w =0
x =0
y =0
z =0

for i in range(N):
    s =input()
    if s =='AC':
        w +=1
    elif s == 'WA':
        x +=1
    elif s == 'TLE':
        y +=1
    elif s == 'RE':
        z +=1

print ('AC x '+str(w))
print ('WA x '+str(x))
print ('TLE x '+str(y))
print ('RE x '+str(z))