X=int(input())

n = 0

big = 0
small=0

#print(10**9)

while True:

   if (n**5 - (n-1)**5) > 10**9 :
     break
   big=n
   n += 1

n=0
while True:
   if (n**5 - (n-1)**5) > 10**9 :
     break
   small=n
   n -= 1

a = list(range(0, big,   1))+list(range(-1, small-1, -1))
b = list(range(0, big-1, 1))+list(range(-1, small-2, -1))

stopFlag = False
for ia in a:
   if stopFlag :
      break
   for ib in b:

     if (ia**5) - (ib**5) == X:
        print(ia, ib)
        stopFlag = True
        break
