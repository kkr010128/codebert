K = int(input())
num = 0
for i in range(0,K+1):
    num = (num*10+7)%K
    if num==0:
        print(i+1,'\n')
        break
if num:
    print("-1\n")