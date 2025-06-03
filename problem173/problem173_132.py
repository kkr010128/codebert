a = int(input())


c=0

for i in range(a + 1):
 	if bool(i%3!=0 and i % 5 != 0):
  		c += i
  
print(c)