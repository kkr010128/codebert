N = int(input())
out_ans = []
while N > 26:
    N -= 1
    out_ans.append(int(N % 26))
    N = (N // 26)
N -= 1
out_ans.append(int(N))
out_dic = ['a', 'b', 'c','d', 'e', 'f','g','h','i','j',
              'k','l','m','n','o','p','q','r','s','t','u','v',
              'w','x','y','z']
ans = ''
for i in range(len(out_ans)-1, -1, -1):
    ans = ans + (out_dic[out_ans[i]])
print(ans)