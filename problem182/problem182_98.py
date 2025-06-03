n,k,c = list(map(int,input().split()));s=[True if i=="o" else False for i in input()]
front=[0]*n;back=[0]*n;count=0
 
day = 0
while day < n:
    if s[day]:
        count += 1
        front[day]= 1
        day += c+1
    else:
        day += 1
    
s = s[::-1]
day = 0
while day < n:
    if s[day]:
        back[day]= 1
        day += c+1
    else:
        day += 1
back = back[::-1]
    
if count ==k:
    for i in range(n):
        if front[i] ==1 and back[i] == 1:
            print(i+1)