A, B = map(int, input().split())

min_ans = int((12.5*A) // 1)
max_ans = int(-((-12.5*(A+1)) // 1))

ans = -1
for i in range(min_ans,max_ans):
  temp_A = (i*0.08)//1
  temp_B = (i*0.1)//1
  if temp_A == A and temp_B == B :
    ans = i
    break
  
print(ans)