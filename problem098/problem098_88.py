n = int(input().rstrip())
red = []
white = []
stones = input().rstrip()
for idx, stone in enumerate(stones):
  if stone == "R":
    red.append(idx)
  if stone == "W":
    white.append(idx)
red_len = len(red)
white_len = len(white)
cnt = 0
for i in range(min(red_len, white_len)):
  red_idx = red[-1-i]
  white_idx = white[i]
  if red_idx> white_idx:
    cnt += 1
  else:
    break
print(cnt)