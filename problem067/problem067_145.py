n = int(input())
count_taro = 0
count_hanako = 0
for i in range(n):
  taro,hanako = map(str, input().split())
  if taro > hanako:
    count_taro += 3
  if hanako > taro:
    count_hanako += 3
  if hanako == taro:
    count_hanako += 1
    count_taro += 1
print(count_taro, count_hanako)
