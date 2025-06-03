'''

'''

INF = float('inf')

def main():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]
    S = [''.join(S[row][col] for row in range(H)) for col in range(W)]
    ans = INF
    for b in range(0, 2**H, 2):
        sections = [(0, H)]
        for shift in range(1, H):
            if (1<<shift) & b:
                sections.append((sections.pop()[0], shift))
                sections.append((shift, H))
        t_ans = len(sections) - 1
        count = {(l, r): 0 for l, r in sections}
        for col in range(W):
            if any(count[(l, r)] + S[col][l:r].count('1') > K for l, r in sections):
                for key in count.keys():
                    count[key] = 0
                t_ans += 1
            for l, r in sections:
                count[(l, r)] += S[col][l:r].count('1')
            if max(count.values()) > K:
                t_ans = INF
                break
        ans = min(ans, t_ans)
    print(ans)


main()
