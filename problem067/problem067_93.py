n=int(input())
tp = 0
hp = 0
for _ in range(n):
    taro,hanaco = input().split()
    if taro == hanaco :
        tp +=1
        hp +=1
    elif taro > hanaco :
        tp += 3
    else: hp += 3
print('{} {}'.format(tp,hp))