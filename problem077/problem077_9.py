a,b,c,d = map(int, input().split())
max_list = [a*c,a*d,b*c,b*d]
max_list = sorted(max_list, reverse=True)
print(max_list[0])
