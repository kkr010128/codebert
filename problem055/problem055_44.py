n = int(input())

L11= [0] * 10
L12= [0] * 10
L13= [0] * 10
L21= [0] * 10
L22= [0] * 10
L23= [0] * 10
L31= [0] * 10
L32= [0] * 10
L33= [0] * 10
L41= [0] * 10
L42= [0] * 10
L43= [0] * 10

for i in range(n):
 b,f,r,v = map(int, input().split())
 r -= 1
 if b == 1:
  if f == 1:
   L11[r] += v
  if f == 2:
   L12[r] += v
  if f == 3:
   L13[r] += v
 if b == 2:
  if f == 1:
   L21[r] += v
  if f == 2:
   L22[r] += v
  if f == 3:
   L23[r] += v
 if b == 3:
  if f == 1:
   L31[r] += v
  if f == 2:
   L32[r] += v
  if f == 3:
   L33[r] += v
 if b == 4:
  if f == 1:
   L41[r] += v
  if f == 2:
   L42[r] += v
  if f == 3:
   L43[r] += v

def PV(L):
 for i in range(9):
  print(" "  + str(L[i]), end="")
 print(" " + str(L[9]))

def PL():
 print("#" * 20)

PV(L11)
PV(L12)
PV(L13)
PL()
PV(L21)
PV(L22)
PV(L23)
PL()
PV(L31)
PV(L32)
PV(L33)
PL()
PV(L41)
PV(L42)
PV(L43)