s = input()
n = len(s)
k = int(input())
start = True
start_count = 0
start_char = s[0]
inside_num = 0
end_count = 0
end_char = ""
memory = s[0]
count = 1
for i in range(1,n):
    if s[i] == memory:
        count += 1
    else:
        if start:
            start_count = count
            start = False
        else:
            inside_num += count//2
        count = 1
        memory = s[i]
end_count = count
end_char = memory
ans = 0
if start_char == end_char:
    if end_count == n:
        ans = n*k//2
    else:
        ans += inside_num*k
        ans += (start_count+end_count)//2*(k-1)+start_count//2+end_count//2
else:
    inside_num += start_count//2
    inside_num += end_count//2
    ans += inside_num*k
print(ans)