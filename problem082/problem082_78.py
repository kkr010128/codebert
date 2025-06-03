def main():
    s = str(input())
    t = str(input())
    s_num = len(s)
    t_num = len(t)
    ans = []
    for i in range(s_num - t_num + 1):
        count = 0
        U = s[i:i + t_num]
        for j in range(t_num):
            if U[j] != t[j]:
                count += 1
        ans.append(count)
    print(min(ans))

main()