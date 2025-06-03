a,b,c =raw_input().split()
a,b,c = map(int,(a,b,c))
ls = list((a,b,c))
ls.sort()
string_ans=''
for k in ls:
    string=''
    string = str(k)+" "
    string_ans = string_ans + string
print string_ans.strip()