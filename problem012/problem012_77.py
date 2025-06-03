a=input()
def ip(a):
    i=2
    while i**2<=a:
        if a%i==0:return False
        i+=1
    return True
b=0
for i in range(int(a)):
    c=input()
    if ip(int(c)):b+=1
print(str(b))