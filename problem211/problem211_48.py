n, rating = map(int, input().split())

if n >= 10:
  print(rating)
if n < 10:
  print(rating + (10 - n)*100)