sen = input()
n = int(input())
for i in range(n):
    cmd = input().split()
    sta = int(cmd[1])
    end = int(cmd[2])
    if cmd[0] == 'replace':
        sen = sen[0:sta] + cmd[3] + sen[end+1:]
    elif cmd[0] == 'reverse':
        rev = sen[sta:end+1]
        rev = rev[::-1]
        # print(rev)
        sen = sen[0:sta] + rev +sen[end+1:]
    elif cmd[0] == 'print':
        print(sen[sta:end+1])
    # print('sen : '+sen)