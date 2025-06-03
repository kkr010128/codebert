def main():
    N = int(input())
    l = []
    for i in range(N):
        l.append(str(input()))
    s_l = set(l)
    print(len(s_l))
main()  