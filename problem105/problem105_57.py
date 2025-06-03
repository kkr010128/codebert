x=int(input())
main=list(map(int,input().split()));count=0
for i in range(len(main)):
    if(main[i]%2!=0 and (i+1)%2!=0): count=count+1
print(count)