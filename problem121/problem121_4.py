n = int(input())
s = ""
al = "abcdefghijklmnopqrstuvwxyz"
 
while n > 0:
  o = (n-1) % 26
  n = (n-1) // 26
  s += al[int(o)]
 
print(s[::-1])