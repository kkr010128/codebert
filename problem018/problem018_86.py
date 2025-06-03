s = input().split(" ")
st = []
for i in range(len(s)):
    if s[i] == "+":
        a = st.pop()
        b = st.pop()
        st.append(a+b)
    elif s[i] == "-":
        a = st.pop()
        b = st.pop()
        st.append(b-a)
    elif s[i] == "*":
        a = st.pop()
        b = st.pop()
        st.append(a*b)
    else:
        st.append(int(s[i]))
print(st[0])