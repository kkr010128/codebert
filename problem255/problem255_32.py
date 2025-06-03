def q_b():
    n = int(input())
    st = input().split()
    s = st[0]
    t = st[1]

    word = []
    for i in range(n):
        word.append(s[i])
        word.append(t[i])
    print("".join(word))

if __name__ == '__main__':
    q_b()