n=int(input())
A=list(map(int,input().split()))
ans=0
for a in A:
    if a%2==0 and a%3!=0 and a%5!=0:
        ans=1
        break
print("ADPEPNRIOEVDE D"[ans::2])