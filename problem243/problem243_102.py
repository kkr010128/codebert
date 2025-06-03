N = int(input())
lists= []
for i in range(N):
    a,b = [x for x in input().split()]
    lists.append([a,int(b)])
X = input()
add_time = False
add = 0
for i in range(N):
    if add_time == True:
        add += lists[i][1]
    if X == lists[i][0]:
        add_time = True

print(add)