from collections import Counter

def solve():
    N = int(input())
    c = Counter([input() for _ in range(N)])
    cnt = -1
    ans = []
    for i in c.most_common():
        if cnt == -1:
            cnt = i[1]
            ans.append(i[0])
        elif cnt == i[1]:
            ans.append(i[0])
        else:
            break
    for a in sorted(ans):
        print(a)
    
if __name__ == "__main__":
    solve()