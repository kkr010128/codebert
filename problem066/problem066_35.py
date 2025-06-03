s_list=[]
while True:
    s = input()#文字列
    if s == "-":
        break
    shuffle = int(input())
    for i in range(shuffle):
        h=int(input())
        s = s[h:]+s[:h]
    s_list.append(s)
for i in range(len(s_list)):
    print(s_list[i])
