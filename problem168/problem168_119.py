days, num = map(int, input().split())
hw = list(map(int, input().split()))
hang = days - sum(hw)
if hang < 0:
  print("-1")
else:
  print(hang)