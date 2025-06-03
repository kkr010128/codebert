s = raw_input()
Q = input()
for q in range(Q):
    str_order = raw_input().split()
    if str_order[0] == 'print':
        print s[int(str_order[1]):int(str_order[2])+1]
    elif str_order[0] == 'reverse':
        start = s[:int(str_order[1])]
        mid = s[int(str_order[1]):int(str_order[2])+1]
        mid = mid[::-1]
        end = s[int(str_order[2])+1:]
        s = start+mid+end
    elif str_order[0] == 'replace':
        start = s[:int(str_order[1])]
        mid = str_order[3]
        end = s[int(str_order[2])+1:]
        s = start+mid+end