N,K = map(int,input().split())
A = list(map(int,input().split()))
already_town_check =[False]*(N+1)
already_town_check[1] = True
already_town = [1]
now_town=1
check=False
my_append = already_town.append
for i in range(K):
    check_town=A[now_town-1]
    if(already_town_check[check_town]):
        cicle_start_value=check_town
        check=True
        break
    already_town_check[check_town]=True
    my_append(check_town)
    now_town = check_town

if(check==False):
    print(now_town)
else:
    cicle_start=already_town.index(cicle_start_value)
    roop_town=already_town[cicle_start:]
    print(roop_town[(K-cicle_start)%((i+1)-cicle_start)])
