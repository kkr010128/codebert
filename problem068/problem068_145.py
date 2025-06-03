def main():
    s = input()
    n = int(input())

    for i in range(n):
        cmds = input().split(' ')

        if 'reverse' == cmds[0]:
            a = int(cmds[1])
            b = int(cmds[2])+1

            s = s[:a]+''.join(reversed(s[a:b]))+s[b:]

        if 'replace' == cmds[0]:
            a = int(cmds[1])
            b = int(cmds[2])+1
            res = cmds[3]

            s = s[:a]+res+s[b:]

        if 'print' == cmds[0]:
            a = int(cmds[1])
            b = int(cmds[2])+1

            print(s[a:b])

if __name__ == '__main__': main()