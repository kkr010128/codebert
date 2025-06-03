h=int(input())
num=1
cnt=0
while h!=1:
    h=h//2
    cnt+=num
    num*=2
cnt+=num
print(cnt)