dice=input().split()
q=int(input())

do = [(2,3,5,4), (6,3,1,4), (2,6,5,1), (2,1,5,6), (1,3,6,4), (2,4,5,3)]

def check(top, front):
    top_index=dice.index(top)
    front_index=dice.index(front)+1
    tmp=do[top_index]
    tmp_index=tmp.index(front_index)
   # print(top_index,front_index,tmp,tmp_index) 
    i = 0
    if tmp_index == 3:
        i = tmp[0]
    else:
        i = tmp[tmp_index+1]
    print(dice[i-1])


for i in range(q):
    top,front=input().split()
    check(top,front)
