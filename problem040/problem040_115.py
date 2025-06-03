num = map(int, raw_input().split())
for i in range(0,2):
 for j in range(0,2):
  if num[j] > num[j+1]:
   tmp_box = num[j]
   num[j] = num[j+1]
   num[j+1] = tmp_box
sort = map(str, num)
print sort[0] + " " + sort[1] + " " + sort[2]