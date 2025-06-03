s=str(input())
s_split=list(s)
s_last=s_split[-1]


if s_last == 's' :
    print(s+'es')
else:
    print(s+'s')