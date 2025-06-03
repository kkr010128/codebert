import sys
sen=[]
for line in sys.stdin:
    sen.append(line)
Sen=''.join(sen)

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
j=[]
k=[]
l=[]
m=[]
n=[]
o=[]
p=[]
q=[]
r=[]
s=[]
t=[]
u=[]
v=[]
x=[]
y=[]
z=[]
w=[]
count={'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z}
for i in range(len(Sen)):
    if Sen[i].isalpha():
        count[Sen[i].lower()].append('#')
for char in sorted(count.keys()):
    print('%s : %d'%(char,len(count[char])))