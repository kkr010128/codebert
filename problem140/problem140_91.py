s=input()


sp=s.replace("?","P")
sd=s.replace("?","D")

d= sd.count('D')+sd.count('DP')
p= sp.count('D')+sp.count('DP')
          
                  
if d < p:
                  
    print(sp)
else:
    print(sd)              
                  
   