#coding: utf-8
string = str(input())
X = 0
li = []
for a in range(len(string)):
    if string[a] == " ":
        li.append(string[X:a])
        X = a+1
li.append(string[X:])
for aa in range(len(li)):
    li[aa] = int(li[aa])
h1 = li[0]
m1 = li[1]
h2 = li[2]
m2 = li[3]
k = li[4]
Time = (h2 * 60 + m2) - (h1 * 60 + m1) - k
print(int(Time))