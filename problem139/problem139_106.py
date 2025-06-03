 
list = input().split()
 
m1 = int(list[0])*60 + int(list[1])
m2 = int(list[2])*60 + int(list[3])
#print(m1,m2)
    
ans = m2 - m1
print(ans-int(list[4]))
