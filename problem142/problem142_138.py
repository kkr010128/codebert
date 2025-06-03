N=list(input())
count="0"
for i in N:
  count=i
if count=="3":
  print("bon")
elif count=="0" or count=="1" or count=="6" or count=="8":
  print("pon")
else:
  print("hon")