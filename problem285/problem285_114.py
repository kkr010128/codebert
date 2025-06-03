def run_length(data, init=''):
    length = []
    tmp = init
    cnt = 0
    for c in data:
        if tmp != c:
            length.append(cnt)
            cnt = 0
        tmp = c
        cnt += 1
    length.append(cnt)
    return length


def resolve():
    s = input()
    if s[0] != '<':
        s = '<' + s
    if s[-1] != '>':
        s = s + '>'

    array = run_length(s)
    ans = 0
    for i in range(1, len(array), 2):
        a,b = array[i], array[i+1]
        mn = min(a,b) - 1
        mx = max(a,b)
        ans += (mn+1) * (mn) // 2 + mx * (mx+1) // 2
    #     print(a,b, (mn+1) * (mn) // 2 + mx * (mx+1) // 2)
    # print(array)
    print(ans)

if __name__ == "__main__":
    resolve()
