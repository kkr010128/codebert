ord_list = []
str_in = input()
n = int(input())

for i in range(n):
    try:
        l = list(map(str,input().split()))
    except ValueError:
        l = list(map(str,input().split()))
    ord_list.append(l)

for l in ord_list:
    o = l[0]
    a,b = int(l[1]), int(l[2])
    if o == 'replace':
        str_in= str_in[:a] + l[3] + str_in[b+1:]
    elif o == 'reverse':
        str_in= str_in[:a] + str_in[a:b+1][::-1] + str_in[b+1:]
    elif o == 'print':
        print(str_in[a:b+1])