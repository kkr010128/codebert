#d 
n=int(input())
x=input()

def popcount(m):
    return bin(m).count("1")

intx = int( "0b"+x ,0 )
popcount0 = x.count("1")

intx_mod_pp1 = intx %(popcount0+1)
if popcount0!=1:
    intx_mod_pm1 = intx %(popcount0-1)
    

jisho = ["yet"]*n
# pow2ip = .5
# pow2im = .5

for i in range(n):
    if x[i]=="1" and popcount0==1:
        print(0)
        continue
    
    pow2ip = pow(2,n-i-1,popcount0+1)
    if popcount0!=1:
        pow2im = pow(2,n-i-1,popcount0-1)

    if False:
        pass
    
    
    else:
        intxi=1
        c=0
        while intxi!=0:
            if c==0:
                if x[i]=="0":
                    pop = popcount0+1
                    intxi = (intx_mod_pp1 + pow2ip%pop )%pop
                else:
                    pop = popcount0-1
                    intxi = (intx_mod_pm1 - pow2im%pop )%pop        
            else:
                if jisho[intxi]=="yet":
                    togo = intxi%popcount(intxi)
                    jisho[intxi]= togo
                    intxi = togo
                else:
                    intxi =jisho[intxi]
                
            #print(intxi)
            c+=1
        print(c)
        #print()
    
#        print("f(n)=",c)