number=list(map(int,input().split()))
count_l=number[0]
count_t=number[1]
luggage=[int(input()) for i in range(count_l)]

min_P=max(max(luggage),sum(luggage)//count_t)
max_P=sum(luggage)
left=min_P
right=max_P

while left<right:
    mid=(left+right)//2
    count_track=1
    flag=1
    load=0
    for i in range(count_l):
        load+=luggage[i]
        if load>mid:
            count_track+=1
            load=luggage[i]

        if count_track>count_t:
            flag=0
            break

    if flag:
        right=mid

    else:
        left=mid+1

print(left)

