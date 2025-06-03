s = input().split()
st = []

for i in range(len(s)):
    c = s.pop(0)
    if c == '+':
        b = st.pop(0)
        a = st.pop(0)
        ans = a + b
        st.insert(0,ans)
    elif c == '-':
        b = st.pop(0)
        a = st.pop(0)
        ans = a - b
        st.insert(0,ans)
    elif c == '*':
        b = st.pop(0)
        a = st.pop(0)
        ans = a * b
        st.insert(0,ans)
    else:
        st.insert(0, int(c))

print(st.pop(0))
