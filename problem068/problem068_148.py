st = input()
q = int(input())

for x in range(q):
    ip = list(input().split())

    if ip[0] == "print":
        print(st[int(ip[1]):int(ip[2])+1])
    elif ip[0] == "replace":
        ip[1] = int(ip[1])
        ip[2] = int(ip[2])
        temp = st[0:ip[1]] + ip[3] + st[ip[2]+1:]
        st = temp
    elif ip[0] == "reverse":
        ip[1] = int(ip[1])
        ip[2] = int(ip[2])
        temp = st[0:ip[1]] + st[ip[1]:ip[2]+1][::-1] + st[ip[2]+1:]
        st = temp




