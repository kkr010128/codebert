n = int(input())
lis = []
#print(n)
alf = ""

while n > 0:
    n -= 1
    mod = n % 26
    lis.insert(0,mod)
    n = n // 26
    #print(n)

for i in lis:
   alf += chr(ord("a") + i)
print(alf)