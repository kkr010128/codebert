def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
 
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
 
   return lcm
 
 
 
num1 = int(input())
a=lcm(num1,360)
b=a/num1
print(int(b))