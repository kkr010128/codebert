a=input()
num=[]
for x in range(int(a)+1):
    if x!=0 and x%3==0 or x%10==3 or "3" in str(x):
        num.append(x)

str_list=map(str,num)
print(" "+" ".join(str_list))