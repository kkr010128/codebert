list_2d=[]
for i in range(3):
    list_2d.append([int(i) for i in input().split()])

n=int(input())

b=[int(input()) for i in range(n)]
#print(list_2d)
#print(b)
 
#印をつける
for i in range(3):
    for j in range(3):
        if list_2d[i][j] in b:
            list_2d[i][j]="x"
            
#print(list_2d)

#ビンゴかどうかチェックする
#横
if list_2d[0]==["x","x","x"] or list_2d[1]==["x","x","x"] or list_2d[2]==["x","x","x"]:
    ans="Yes"
    
#縦
elif list_2d[0][0]==list_2d[1][0]==list_2d[2][0]=="x" or  list_2d[0][1]==list_2d[1][1]==list_2d[2][1]=="x" or  list_2d[0][2]==list_2d[1][2]==list_2d[2][2]=="x":
    ans="Yes"

#斜め
elif  list_2d[0][0]==list_2d[1][1]==list_2d[2][2]=="x" or  list_2d[0][2]==list_2d[1][1]==list_2d[2][0]=="x":
    ans="Yes"
    
else:
    ans="No"
    
print(ans)