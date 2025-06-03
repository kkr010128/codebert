N = input()
A=[]
for i in N:
    A.append(i)

hon = ["2","4","5","7","9"]
pon = ["0","1","6","8"]
bon = ["3"]
if A[-1] in hon:
    print("hon")
elif A[-1] in pon:
    print("pon")
else:
    print("bon")