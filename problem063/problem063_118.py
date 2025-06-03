import string as st
string=[]
try:
    while True:
        s = input()#入力
        string =list(string)#list変換
        if not s :#空入力のときループぬける
            break
        string.extend(s)#list追加
        string=map(str,string)
        string="".join(string).lower()#str型変換と小文字
except EOFError:
    for i in range(len(st.ascii_lowercase)):
        print("{} : {}".format(st.ascii_lowercase[i],string.count(st.ascii_lowercase[i])))
