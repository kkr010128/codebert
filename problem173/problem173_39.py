n = int(input())
c = 0

for i in range(1,n+1):
    if i%3 or i%5 == 0:
        c += 0
    if i%3 != 0 and i%5 != 0 :
        c += i
print(c)