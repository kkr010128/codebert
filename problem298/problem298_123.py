n=input().split()
h=input().split()
count=0
for i in range(len(h)):
    if int(h[i])>=int(n[1]):
        count+=1
print(count)
