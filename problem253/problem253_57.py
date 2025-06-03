import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n,a,b=map(int, input().split())
    if (abs(a-b))%2==0:
        print((abs(a-b))//2)
    else:
        ue=max(a,b)-1
        sita=n-min(a,b)
        hokasita=((n-max(a,b))*2+1+abs(b-a))//2
        hokaue=(((min(a,b))-1)*2+1+abs(b-a))//2
        print(min(ue,sita,hokasita,hokaue))
resolve()
