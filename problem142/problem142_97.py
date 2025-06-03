m=input()

l=len(m)

if m[l-1]=="0" or m[l-1]=="1" or m[l-1]=="6" or m[l-1]=="8":
 print("pon")
elif m[l-1]=="3":
 print("bon")
else:
 print("hon")