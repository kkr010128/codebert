data=str(input("")).split(" ")
D=int(data[0])
T=int(data[1])
S=int(data[2])

if D<=T*S:
  print("Yes")
else:
  print("No")