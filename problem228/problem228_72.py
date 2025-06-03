H = int(input())

i = 1
cnt = 0

while H > 0:
  H //= 2
  cnt += i
  i *= 2
  
print(cnt)