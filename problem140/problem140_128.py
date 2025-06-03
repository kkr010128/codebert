string = input()
string=list(string)

count = len(string)
summary = 0

for i in range(count):
    if string[i]=="?":
        string[i]="D"
#print(string)

for i in string:
    print(i, end="")