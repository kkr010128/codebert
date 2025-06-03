N=int(input())
x=input()
def popcount(X,ones,count): 
    #print(count,bin(X),X,ones)
    if ones==0:
        return count
    else:
      
        X=X%ones
        
        count+=1
 
        ones=str(bin(X)).count("1")
        
        return popcount(X,ones,count)
 

    
GroundOnes=x.count("1")
GroundX=int(x,2)

if GroundOnes>1:
    CaseOne= GroundX%(GroundOnes-1)
else:
    CaseOne=2

CaseZero= GroundX%(GroundOnes+1)

TwoPowerCaseOne=[]
TwoPowerCaseZero=[]

# if GroundOnes>1:
#     for j in range(N):
#       TwoPowerCaseOne.append(pow(2,(N-j-1) , (GroundOnes-1)))
#       TwoPowerCaseZero.append(pow(2**(N-j-1), (GroundOnes+1)))
# else:
#     for j in range(N):
#       TwoPowerCaseZero.append(pow(2**(N-j-1), (GroundOnes+1)))
  
    
for i in range(N):
    
    #CaseOne
    if x[i]=="1":
        ones=GroundOnes-1
        if ones>0:
            X=CaseOne-pow(2,N-i-1,ones)
        else:
            X=0
    #CaseZero
    else:
        ones=GroundOnes+1
        X=CaseZero+pow(2,N-i-1,ones)
            
 
    # print("for loop",i)
    # print("ones",ones)
    # print("new2bit",new2bit)
    #print(" ------ return --- ",popcount(X,ones,0))
    print(popcount(X,ones,0))