n = int(input())
string = input()
ans = 0
for i in range(0, n-2):
  if string[i] == "A" and string[i+1] == "B" and string[i+2] == "C": ans += 1
    
print(ans)