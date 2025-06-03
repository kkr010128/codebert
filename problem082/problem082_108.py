s=input()
t=input()

count_min = 1000

for i in range(len(s)-len(t)+1):
  count = 0
  for j in range(len(t)):
    if s[i+j] != t[j]:
      count+=1 
  if count < count_min:
    count_min = count

print(count_min)