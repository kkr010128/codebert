h=int(input())
def attack(n):
  if n==1:
    return 1
  else:
    return 1+2*attack(n//2)

print(attack(h))


