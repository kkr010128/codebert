N = int(input())
A = list(map(int, input().split()))

kane=1000
kabu=0
for i in range(N-1):
    #print(kane,kabu)
    
    if A[i]<A[i+1]:
        kane=kabu*A[i]+kane
        kabu=kane//A[i]
        kane=kane-kabu*A[i]
    else:
        kane=kabu*A[i]+kane
        kabu=0
        
print(kane+kabu*A[N-1])