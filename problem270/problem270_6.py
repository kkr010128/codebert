a=["SUN","MON","TUE","WED","THU","FRI","SAT"]
s=input()
k=-1
for i in range(7):
    if(a[i]==s):k=i
k=(7-k)
print(k)