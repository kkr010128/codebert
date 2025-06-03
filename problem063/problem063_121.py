import collections

n = []

while True:
   try:
       N = input()
   
   except EOFError:
       break
   
   N = N.lower() 
    
   N.replace('', ' ')
   
   n.extend(N)
   
c = collections.Counter(n)

for i in range(97, 97+26):
        print("%s : %d" % (chr(i),c[chr(i)]) )

