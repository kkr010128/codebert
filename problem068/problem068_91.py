str = raw_input()
q = input()
for ans in range(q):
    ans = raw_input()
    ans1 = ans.split(' ')
    if ans1[0] == 'replace':
        str = str[0:int(ans1[1])]+ans1[3]+ str[int(ans1[2])+1:len(str)]
    if ans1[0] == 'reverse':
        str = str[0:int(ans1[1])]+ str[int(ans1[1]):int(ans1[2])+1][::-1] + str[int(ans1[2])+1:len(str)]
    if ans1[0] == 'print':
        print str[int(ans1[1]):int(ans1[2])+1]