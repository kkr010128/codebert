NUM=1000

X=int(input())

flg=False

for i in reversed(range(NUM)):
    for j in range(-1*NUM,NUM):
        res=(i**5)-(j**5)
        if res==X:
            ans_A=i
            ans_B=j
            flg=True
            break
    if flg:
        break

print(ans_A,ans_B)