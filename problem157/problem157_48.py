def resolve():
    n = int(input())
    a = list(map(int, input().split()))

    dict1 = {}
    dict2 = {}

    for i in range(n):
        a1 = a[i] + i + 1
        a2 = i + 1 - a[i]
        if a1 in dict1:
            dict1[a1] += 1
        else:
            dict1[a1] = 1
        if a2 in dict2:
            dict2[a2] += 1
        else:
            dict2[a2] = 1
    ans = 0
    for i in dict1:
        if i in dict2:
            ans += dict1[i]*dict2[i]
    print(ans)
            
resolve()