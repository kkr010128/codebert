n=int(input())
s = input()
Ra = s.count('R')
t = s[:Ra]
Rb = t.count('R')
print(Ra-Rb)