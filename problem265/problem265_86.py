N = int(input())
 
for i in range(1, N + 1):
  if i + (i * 8) // 100 == N:
    print(i)
    break
else:
  print(":(")