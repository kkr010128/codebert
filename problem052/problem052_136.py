n=input()
s=''
for i in range(1,int(n)+1):
    s += (' '+str(i)) if i%3==0 or '3' in str(i) else ''
print(s)