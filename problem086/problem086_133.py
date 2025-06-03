n,x,t = input().split(" ")

s = 0
time = 0
while int(n) > s:
  s += int(x)
  time += int(t)
print(time)