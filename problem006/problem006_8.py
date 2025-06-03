a=100000
n=int(input())
for i in range(n):
    a=a*1.05
    if a%1000 !=0:
        a=a-(a%1000)+1000
print(int(a))

