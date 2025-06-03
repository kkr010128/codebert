a=int(input())
count1=0
count2=0
count3=0
count4=0
for i in range(a):
    b=str(input())
    count=0
    if b=='AC':
        count1+=1 
       
    if b=='RE':
        count2+=1 
       
    if b=='TLE':
        count3+=1 
       
    if b=='WA':
        count4+=1 
print('AC x ',end='')
print(count1)
print('WA x ',end='')
print(count4)
print('TLE x ',end='')
print(count3)
print('RE x ',end='')
print(count2)