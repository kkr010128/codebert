str = input()
cnt = 0
if str[0]=="R" and str[1]=="R" and str[2]=="R":
  cnt = 3
elif (str[0]=="R" and str[1]=="R") or (str[1]=="R" and str[2]=="R"):
  cnt = 2
elif str[0]=="R" or str[1]=="R" or str[2]=="R":
  cnt = 1
print(cnt)