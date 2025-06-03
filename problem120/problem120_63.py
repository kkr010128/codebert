a=input()
l=a.split(" ")
n=int(l[0])
k=int(l[1])
f=input()
fruits=f.split(" ")
for d in range(0, len(fruits)):
    fruits[d]=int(fruits[d])
ans=0
b=0
while(b<k):
    g=min(fruits)
    ans+=g
    fruits.remove(g)
    b+=1
print(ans)