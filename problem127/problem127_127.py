X,Y = map(int,input().split())

ans='No'
for i in range(0,X+1):
   #print(i)
   if i * 2 + (X - i) * 4 == Y and X>=i:
       ans = 'Yes'
       break

print(ans)