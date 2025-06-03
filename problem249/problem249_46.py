taka, aoki, num = map(int, input().split())
if taka <= num:
  num -= taka
  taka = 0
  if aoki <= num:
    aoki = 0
    print(taka, aoki)
  elif aoki > num:
    aoki -= num
    print(taka, aoki)  
if taka > num:
  taka -= num
  print(taka, aoki)
