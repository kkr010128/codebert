
N = int(input())
table = list(map(int,input().split()))

MAX = 2000
check = [False]*(MAX+1)

def recursive(index,tmp_sum):
    global N

    if index == N:
        check[tmp_sum] = True
        return

    recursive(index+1,tmp_sum)
    if tmp_sum+table[index] <= MAX:
        recursive(index+1,tmp_sum+table[index])

recursive(0,0)

num_query = int(input())
for num in list(map(int,input().split())):
    if check[num]:
        print("yes")
    else:
        print("no")
