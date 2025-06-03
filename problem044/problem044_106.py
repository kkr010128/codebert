a,b,c = (int(x) for x in input().split())
count = 0

while a <= b:
  if c % a == 0:
    count += 1
  a += 1

print (str(count))
