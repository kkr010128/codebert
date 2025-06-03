#a = list(map(int,input().split()))
#b = list(map(int,input().split()))

a = int(input())
x = int(100)
count= 0
while a > x:
    count+=1
    x += x//100
print(count)