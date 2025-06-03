a=input()
b=a.split(" ")
c=list(map(int,b))
w=c[0]
h=c[1]
x=c[2]
y=c[3]
r=c[4]
if((x-r)<0 or (x+r)>w or (y-r)<0 or (y+r)>h):
    str="No"
else :
    str="Yes"
print(str)