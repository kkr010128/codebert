S = int(input())
if S<3:
    print(0)
    exit()

clear = 0
memory = dict()

def hoge(S):
    clear = 0
    i = 3
    while True:
        if (S-i)==0:
            clear+=1
            break
        elif S-i in memory:
            clear += memory[S-i]
        elif S-i>=3:
            memory[S-i] = hoge(S-i)
            clear += memory[S-i]
        i += 1
    return clear


print(hoge(S)%(10**9+7))
