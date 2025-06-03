H,A = map(int, input().split())
cnt = H//A
if (H%A):
  cnt +=1
print(cnt)