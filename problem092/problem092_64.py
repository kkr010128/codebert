x,k,d = list(map(int, input().split()))
amari = abs(x) % d
shou = abs(x) // d

amari_ = abs(amari - d)
if k < shou:
  print(abs(x) - d * k)
else:
  if (k - shou) % 2 == 0:
    print(amari)
  else:
    print(amari_)