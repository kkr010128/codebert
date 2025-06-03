line = input().split()

total = int(line[0])
lim = int(line[1])
time = int(line[2])

ans = total//lim
amari = total%lim

if amari == 0:
  ans2 = ans*time
else:
  ans2 = (ans + 1)*time 

print(ans2)