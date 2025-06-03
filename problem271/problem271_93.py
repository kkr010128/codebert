N=int(input())
S=input()
a=ord("A")
z=ord("Z")
result=""
for i in range(len(S)):
    word=ord(S[i])+N
    if word>z:
        word=word-z-1+a
    x=chr(word)
    result+=x
print(result)
