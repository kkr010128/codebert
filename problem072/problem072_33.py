n =int(input())
first =[]
second =[]
for i  in range(n):
    d1 , d2 = map(int , input().split())
    first.append(d1)
    second.append(d2)

for i in range(n-2):
    count = 0
    for j in range(i ,i+3):
        if first[j]==second[j]:
            count +=1
        else:
            break
           
    if count ==3:
        print("Yes")
        break
    
else:
    print("No")