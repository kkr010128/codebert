n = int(input())
s = input()

sl = list(s)

answer = ""
for i in s:
  t = ord(i)+n
  if t <= 90:
    answer += chr(t)
  else :
    answer += chr(ord("A") + abs(t-90)-1)

print(answer)