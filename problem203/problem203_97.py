A,B=map(int,input().split())
c=-1
for i in range(1,10**5):
    if int(i*0.08)==A and int(i*0.1)==B:
        c=i
        break
print(c)