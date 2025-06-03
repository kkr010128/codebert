n=int(input())
i=int(n**0.5)
while n%i:
    i-=1
print(i+n//i-2)