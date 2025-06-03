N = int(input())
p_list = []
for i in range(N):
  s = input().split(' ')
  p_list.append(s)
X = input()
flg = False
time = 0
count = 0
for sound in p_list:
  if sound[0] == X:
    time = int(sound[1])
    flg = True
  if flg:
    count += int(sound[1])
print(count-time)