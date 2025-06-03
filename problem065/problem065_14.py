w = input().lower()
c = 0
while True:
   t = input()
   if t == "END_OF_TEXT":
       break
   t = t.lower()
   t = t.rstrip().split()
   c += t.count(w)
print(c)

 
