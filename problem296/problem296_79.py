s=list(input())
a=int(input())

w = ""
c = 0
cnt = 0
for i in s:
    if w != i:
        #print(w)
        cnt += c//2
        c = 1
        w = i
    else:
        c +=1
cnt += c//2
#print(cnt)

start = 0
start_w = s[0]
for i in s:
    if start_w != i:
        break
    else:
        start +=1

s.reverse()

end = 0
end_w = s[0]
for i in s:
    if end_w != i:
        break
    else:
        end +=1

same = len(list(set(s)))
#print(same)

if s[0] != s[-1]:
    print(cnt*a)
elif same ==1:
    print(len(s)*a//2)
else:
    print(cnt*a-(a-1)*(start//2+end//2-(start+end)//2))