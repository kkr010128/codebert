n=int(input())
I=list(map(int,input().split()))
for i in range(n):
    if (I[i]%2==0):
        if (I[i]%3!=0) and (I[i]%5!=0):
            print("DENIED")
            exit()
print("APPROVED")            
