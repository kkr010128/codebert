n=int(input())
A=list(map(int,input().split()) )
q=int(input())
B=[]
C=[]

a_sum = sum(A)
counter = [0]*10**5

for a in A:
    counter[a-1] += 1

for i in range(q):
    b,c = map(int,input().split()) 
       
    a_sum += (c-b) * counter[b-1]
      
    counter[c-1]+=counter[b-1]
    counter[b-1]=0
    
    print(a_sum)
