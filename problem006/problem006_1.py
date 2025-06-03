a=100000

for i in range(int(input())):
    a *=1.05
    if a%1000 !=0:
        a=a-(a%1000)+1000
        
print(int(a))
    

