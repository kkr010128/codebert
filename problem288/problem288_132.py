N = int(input())
root = int(N**0.5)
for i in range(root,-1,-1):
  if N % i ==0:
    break

print(int(N/i + i -2))
