a,b = map(int,input().split())
if a%2 == 0:
  	a_list = [int(a/0.08) + i for i in range(13)]
else:
  	a_list = [int(a/0.08) + i for i in range(1,13)]
b_list = [int(b/0.1) + j for j in range(10)]
com = set(a_list) & set(b_list)
if len(com) == 0:
    print(-1)
elif len(com) != 0:
    if int(min(com)*0.08) != a or int(min(com)*0.1) != b:
        print(-1)
    else:
        print(min(com))