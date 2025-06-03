s = input()
t = s[::-1]

cnt = 0
for i, j in zip(s, t):
  if i != j:
    cnt += 1
    
print(cnt // 2)