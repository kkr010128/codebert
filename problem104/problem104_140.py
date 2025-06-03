from sys import stdin,stdout
l,r,d=list(map(int,stdin.readline().strip().split()))
c=0
if l%d==0 and r%d==0:
    stdout.write(str(int(r/d)-int(l/d)+1)+'\n')
else:
    stdout.write(str(int(r/d)-int(l/d))+'\n')
