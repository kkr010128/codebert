#x,a=[int(x) for x in input().split]t,input()
x,a=map(int,input().split())
counter=0
while(x>0):
    x-=a
    counter+=1
print(counter)
