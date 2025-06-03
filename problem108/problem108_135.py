a = int(input())
num = a //1000
b = num*1000 - a
if b < 0:
    c = (num+1)*1000-a
    print(c) 
else:
    print(b)

 

