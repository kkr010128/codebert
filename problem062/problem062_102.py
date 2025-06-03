sum = [] 

while True:
    text = input()

    if text == '0':
        break

    tmp = 0
    for i in range(len(text)):
       tmp += int(text[i]) 
    sum.append(tmp)

for r in sum:
    print(r)