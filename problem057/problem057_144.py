date=[[],[],[]]
a,b,c=0,0,0
while True:
   if a < 0 and b < 0 and c < 0:
      break
   else:
      a,b,c =[int(i) for i in input().split()]
      date[0].append(a)
      date[1].append(b)
      date[2].append(c)
for h in range(0,len(date[0])-1):
   if date[0][h] == -1 or date[1][h] == -1:
      print("F")
   elif date[0][h] == date[1][h] == date[2][h]:
      break
   else:
      if date[0][h] + date[1][h] >= 80:
         print("A")
      else:
         if date[0][h] + date[1][h] >= 65:
            print("B")
         else:
            if date[0][h] + date[1][h] >= 50:
               print("C")
            else:
               if date[0][h] + date[1][h] >=30:
                  if date[2][h] >= 50:
                     print("C")
                  else:
                     print("D")
               else:
                  print("F")