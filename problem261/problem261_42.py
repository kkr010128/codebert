S = input()
a = len(S)
count = 0
for i in range(a):
  if S[i] != S[-(i+1)]:
    count += 1
if a%2 ==0:
  print(int(count/2))
else:
  print(int((count +1)/2))