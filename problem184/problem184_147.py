answer = input()

count = 0
list = []
for i in answer:
    list.append(i)

if len(answer) != 6:
    print("No")

elif list[2] == list[3] and list[4] == list[5]:
    print("Yes")

else:
    print("No")
