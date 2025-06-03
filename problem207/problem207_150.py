AA1 = input().split()
AA2 = input().split()
AA3 = input().split()
AA4 = [AA1[0],AA2[0],AA3[0]]
AA5 = [AA1[1],AA2[1],AA3[1]]
AA6 = [AA1[2],AA2[2],AA3[2]]
AA7 = [AA1[0],AA2[1],AA3[2]]
AA8 = [AA1[2],AA2[1],AA3[0]]
N = int(input())
list1 = []
for i in range(N):
  b = input()
  list1.append(b)
count = 0
bingo =0
for i in list1:
  if i in AA1:
    count +=1
if count ==3 :
  bingo =1
else:
  count =0
  
for i in list1:
  if i in AA2:
    count +=1
if count ==3 :
  bingo =1
else:
  count =0

for i in list1:
  if i in AA3:
    count +=1
if count ==3 :
  bingo =1
else:
  count =0
  
for i in list1:
  if i in AA4:
    count +=1
if count ==3 :
  bingo =1
else:
  count =0

for i in list1:
  if i in AA5:
    count +=1
if count ==3 :
  bingo =1
else:
  count =0

for i in list1:
  if i in AA6:
    count +=1
if count ==3 :
  bingo =1
else:
  count =0
  
for i in list1:
  if i in AA7:
    count +=1
if count ==3 :
  bingo =1
else:
  count =0
for i in list1:
  if i in AA8:
    count +=1
if count ==3 :
  bingo =1
else:
  count =0
if bingo ==1:
  print('Yes')
else:
  print('No')