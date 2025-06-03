s = input()
k = int(input())
n = len(s)
renzoku_flag =False
renzoku_count = 0
count = 0
for i in range(n):
    if i != n-1:
        if s[i] == s[i+1]:
            renzoku_count += 1 #iのをカウントしている
        else:
            renzoku_count += 1 #i+1の分をカウント
            count += renzoku_count // 2
            renzoku_count = 0
    else:
        if s[n-2] == s[n-1]:
            renzoku_count += 1
        count += renzoku_count // 2

if s[0] != s[-1]:
    print(count*k)
else:
    ans = count*k
    initial = s[0]

    start_count = 0
    for i in range(n):
        if s[i] == initial:
            start_count += 1
        else:
            break
    else:
        print(n*k//2)
        exit()

    end_count = 0
    for i in range(n)[::-1]:
        if s[i] == initial:
            end_count += 1
        else:
            break

    ans -= (start_count//2 + end_count//2 - (start_count+end_count)//2)*(k-1)
    print(ans)
