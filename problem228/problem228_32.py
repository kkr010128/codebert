H = int(input())
def atk(n):
  if n==1: return 1
  return 1 + 2*(atk(n//2))

print(atk(H))