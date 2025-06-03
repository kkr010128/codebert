n = int(input())
root = int(n**0.5)

yakusu = 0

for i in range(root, 0, -1):
  if n % i == 0:
    yakusu = i
    break

another = n // yakusu

print(yakusu + another - 2)