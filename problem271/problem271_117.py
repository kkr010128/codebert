n=int(input())
s=input()
l=[]
for i in s:
    x=(ord(i)-65+n)%26
    y=chr(65+x)
    l.append(y)
print(''.join(l))
