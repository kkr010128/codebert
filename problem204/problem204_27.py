def main():
    import sys
    s = input()
    q =int(input())
    ten = 0
    r = []
    l = []
    for _ in range(q):
        ls = tuple(map(str, sys.stdin.readline().split()))
        if len(ls)==1:
            ten +=1
        else:
            if ls[1] =='1':
                if ten%2 ==0:
                    l.append(ls[2])
                else:
                    r.append(ls[2])
            else:
                if ten%2 ==1:
                    l.append(ls[2])
                else:
                    r.append(ls[2])
    s = ''.join(reversed(l))+s+''.join(r)
    if ten%2 ==1:
        s = s[::-1]
    print(s)
if __name__ == '__main__':
    main()