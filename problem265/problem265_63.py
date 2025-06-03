N = int(input())

for x in range(50001):
  y = int( x * 1.08 )
  if y == N:
    print(x)
    exit()
    
print(":(")