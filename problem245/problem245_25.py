n = int(input())
s = input()
count = 0
for i in range(len(list(s))-2):
  if s[i] == "A" and s[i+1] == "B" and s[i+2] =="C":
    count += 1
print(count)