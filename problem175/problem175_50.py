l =int(input())
s =input()
r = s.count("R")
g = s.count("G")
b = s.count("B")
A = r * g * b
B = 0
gapmax = (l - 3) // 2
for _ in range(gapmax+1):
  for i in range(l-2-2*_):
    c1, c2, c3 = s[i], s[i+1+_],s[i+2+2*_]
    if not (c1 == c2) and not (c1 == c3) and not (c2 ==c3):
      B += 1
      
print(A-B)