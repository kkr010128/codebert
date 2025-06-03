l=list(input().split())  ##文字も数字も入る
stack=[]

for x in l: ##リストの長さ文だけ繰り返し
    if x in ['+','-','*']: ##←知らなかった判定方法
        t=str(stack.pop()) ##末尾取り出し
        r=str(stack.pop())
        c=r+x+t
        stack+=[int(eval(c))] ##eval:入力した式の入力

    else:
        stack+=[int(x)] ##[]の意味?>リストに追加

print(stack.pop())

