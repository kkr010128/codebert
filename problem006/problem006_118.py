n=int(input())
x=100000
for i in range(n):
    x=x+x*0.05
    x=((x-1)//1000+1)*1000
print(int(x))
