N = input()
inpa = input().split(" ")
count =0
for x in range(0,int(N),2):
    if int(inpa[x])%2==1:
        count = count + 1
print(count)