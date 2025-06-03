N = int(input())
 
count = 0
 
for i in range(1,N):
        if int(N/i)-N/i == 0:
            count += int(N/i)-1
        else:
            count += int(N/i)
 
 
 
print(count)