import collections
s = str(input())
k = int(input())

ans = 0
#if s[0] == s[-1]:
#    ans += k

tmp = ''
tmp_num = 0

check = ''
check_num = 0

if len(collections.Counter(s).keys()) == 1:
    ans = len(s)*k//2

else:
    for i, w in enumerate(s):
        if i == 0:
            tmp += w
            tmp_num += 1
            continue
        
        if tmp[-1] == w:
            tmp += w
            tmp_num += 1
        
        elif tmp[-1] != w:
            if check_num == 0:
                check = tmp
                check_num = 1

            ans += (tmp_num // 2) * k
            #print('ans', ans)
            tmp = w
            tmp_num = 1
        
        if i == len(s)-1:
            if len(tmp) == 1:
                if check[0] == tmp and (len(tmp)%2 == 1 and len(check)%2 == 1):
                    ans += k-1
            else:
                #print(check, tmp)
                if check[0] == tmp[-1] and (len(tmp)%2 == 1 and len(check)%2 == 1):
                    ans += k-1

            ans += (tmp_num // 2) * k
            #print('last', ans)

print(ans)

