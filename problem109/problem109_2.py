n = int(input())
a = 0
w = 0
t = 0
r = 0
for i in range(n):
  s = input()
  if s == 'AC':
    a+=1
  elif s =='WA':
    w +=1
  elif s =='TLE':
    t +=1
  else:
    r+=1
print('AC x '+str(a))
print('WA x '+str(w))
print('TLE x '+str(t))
print('RE x '+str(r))