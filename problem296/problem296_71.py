s = input()
k = int(input())
li = list(s)
lee = len(s)

if len(list(set(li))) == 1:
    print((lee)*k//2)
    exit()


def motome(n,list):
    count = 0
    kaihi_flag = False
    li = list*n
    for i,l in enumerate(li):
        if i == 0:
            continue
        if l == li[i-1] and not kaihi_flag:
            count += 1
            kaihi_flag = True
        else:
            kaihi_flag = False
    #print(count)
    #print(count*k)
    return count

if k >= 5 and k%2 == 1:
    a = motome(3,li)
    b = motome(5,li)
    diff = b - a
    ans = b + (k-5)//2*diff
    print(ans)
elif k >=5 and k%2 == 0:
    a = motome(2,li)
    b = motome(4,li)
    diff = b - a
    ans = b + (k-4)//2*diff
    print(ans)
else:
    count = 0
    kaihi_flag = False
    li = li*k
    for i,l in enumerate(li):
        if i == 0:
            continue
        if l == li[i-1] and not kaihi_flag:
            count += 1
            kaihi_flag = True
        else:
            kaihi_flag = False
    #print(count)
    #print(count*k)
    print(count)
