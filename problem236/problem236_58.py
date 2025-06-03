hei = int(input())
wei = int(input())
n = int(input())
kuro =0
count = 0

if hei > wei:
  data = hei
else:
  data = wei 
while kuro<n:
  kuro +=data 
  count +=1
print(count)