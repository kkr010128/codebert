name = input()
length = len(name)

if "s" == name[length-1]:
  name = name + "es"
else:
  name = name + "s"

print(name)