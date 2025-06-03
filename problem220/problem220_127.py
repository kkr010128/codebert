S,T=input().split()
num1,num2=map(int,input().split())
throw=input()

if throw==S:
    num1-=1
else:
    num2-=1
    
print(num1,num2)    