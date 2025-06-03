S=input()
Q=int(input())
reverse=False
front=""
rear=""
for _ in range(Q):
    inp=input()
    if inp[0]=="1":
        reverse= not reverse
    elif inp[0]=="2":
        if (inp[2]=="1" and not reverse) or (inp[2]=="2" and reverse):
            front=inp[4]+front
        else:
            rear=rear+inp[4]
ans=front+S+rear
if reverse:
    ans=ans[::-1]
print(ans)