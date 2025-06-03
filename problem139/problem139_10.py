h1,m1,h2,m2,k =(int(x) for x in input().split())  
 
hrtom= (h2-h1)
 
if (m2-m1 < 0) and (h2-h1 >=0) : 
    min = (h2-h1)*60 + (m2-m1) - k
    print(min)
    
elif (m2-m1 >= 0) and (h2-h1 >=0 ):
    min = (h2-h1)*60 + (m2-m1) - k 
    print(min)

    

else:
    print('0')