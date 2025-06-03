marks=[]
while True:
    s=input().split()
    marks.append(s)
    if ["-1","-1","-1"] in marks:
        break
marks=marks[:-1]
for i in marks:
    if int(i[0])==-1 or int(i[1])==-1:
        print("F")
    elif int(i[0])+int(i[1])>=80:
        print("A")
    elif 65<=int(i[0])+int(i[1])<80:
        print("B")
    elif 50<=int(i[0])+int(i[1])<65:
        print("C")
    elif 30<=int(i[0])+int(i[1])<50:
        if int(i[2])>=50:
            print("C")
        else:
            print("D")
    elif int(i[0])+int(i[1])<30:
        print("F")
