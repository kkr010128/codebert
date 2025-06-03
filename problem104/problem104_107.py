# coding: utf-8
# Your code here!

a,b,c=input().split()

#print(a)
#print(b)
#print(c)

i=0
num=int(a)
count=0

while(i!=int(b)-int(a)+1): 
    #print("1")
    if (num%int(c)==0):
        count+=1
    num+=1
    i+=1
print(count)
