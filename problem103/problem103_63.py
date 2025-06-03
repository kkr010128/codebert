N= int(input())
A = list(map(int,input().split()))
A.insert(0,A[0])
A.append(0)
 
money = 1000
previous_tendency = "remain"
current_tendency = "remain"
count = 1

#print(A)
 
for n in range(1,len(A)-1):
    if A[n] < A[n+1]:
        current_tendency = "up"
    elif A[n] > A[n+1]:
        current_tendency = "down"
    else:
        current_tendency = "remain"
        
    if previous_tendency != "down" and current_tendency != "up":
        #print(money,n,"chance",A[n],min(A[count:n+1]),previous_tendency, current_tendency)
        money += (money//min(A[count:n+1]))*(A[n]-min(A[count:n+1]))
        #print(A[count:n+1],money)
        count = n + 1
        previous_tendency = "remain"
    #print(A[n],max_price,min_price,previous_tendency,current_tendency)
    
    if current_tendency != "remain":
      previous_tendency = current_tendency
print(money)