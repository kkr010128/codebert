n=int(input())
l=""
for i in range(1,n+1):
    if i % 3==0 or i % 10 == 3 or (i % 100)//10 == 3 or (i % 1000)//100 == 3 or (i % 10000)//1000 == 3:
        l+=" "+str(i)
print(l)
