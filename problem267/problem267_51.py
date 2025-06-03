n=int(input())
s=input()
cnt=0
def judge(n):
    pos=0
    pos=s.find(n[0],pos)
    if pos==-1:
        return 0
    pos=s.find(n[1],pos+1)
    if pos==-1:
        return 0
    pos=s.find(n[2],pos+1)
    if pos==-1:
        return 0
    return 1
for i in range(1000):
    p=str(i).rjust(3,'0')
    if judge(p):
        cnt+=1
print(cnt)