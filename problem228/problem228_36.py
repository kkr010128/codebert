H = int(input())

c=1
h=H
while 1:
    h = h//2
    if h==0 :
        break
    c+=(1+c)

print(c)
