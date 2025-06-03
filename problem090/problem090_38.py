'''
def main():
    S = input()
    cnt = 0
    ans = 0
    f = 1
    for i in range(3):
        if S[i] == 'R':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)
'''
def main():
    S = input()
    p = S[0] == 'R'
    q = S[1] == 'R'
    r = S[2] == 'R'

    if p and q and r :
        print(3)
    elif (p and q) or (q and r):
        print(2)
    elif p or q or r:
        print(1)
    else:
        print(0)
    


if __name__ == "__main__":
    main()