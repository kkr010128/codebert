inArray = str(input()).split(" ")
if int(inArray[0]) < int(inArray[-1]):
  print("a < b")
elif int(inArray[0]) > int(inArray[-1]):
  print("a > b")
else:
  print("a == b")
