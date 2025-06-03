n = int(input())
a = int(n//1.08)
for x in range(a, a+2):
  if x < (n + 1)/1.08 and x >= n/1.08:
    print(x)
    exit()
print(':(')