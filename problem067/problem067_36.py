n = int(input())
s_taro,s_hanako = 0,0

for trial in range(n):
    taro,hanako = list(map(str, input().split()))
    if taro > hanako:
        s_taro += 3
    elif taro < hanako:
        s_hanako += 3
    else:
        s_taro += 1
        s_hanako += 1

print(s_taro, s_hanako)