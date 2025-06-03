k = int(input())

num=[1,2,3,4,5,6,7,8,9]

if k<10:
    print(num[k-1])
    exit()

ans=9

def hantei():
    global ans
    ans+=1
    if ans==k:
        print(num[-1])
        exit()

for i in range(10**10):

    hitoketa=num[0]%10

    if hitoketa==0:
        num.append(10*num[0]+0)
        hantei()
        num.append(10*num[0]+1)
        hantei()
        num.pop(0)

    elif hitoketa==9:
        num.append(10*num[0]+8)
        hantei()
        num.append(10*num[0]+9)
        hantei()
        num.pop(0)

    else:
        num.append(10*num[0]+(hitoketa-1))
        hantei()
        num.append(10*num[0]+(hitoketa))
        hantei()
        num.append(10*num[0]+(hitoketa+1))
        hantei()
        num.pop(0)