n = int(input())
t_count = 0
h_count = 0
for i in range(n):
    t_animal,h_animal = map(str,input().split())
    if t_animal < h_animal:
        h_count+=3
    elif t_animal > h_animal:
        t_count+=3
    else:
        t_count+=1
        h_count+=1
print("{} {}".format(t_count,h_count))
