from collections import deque

def main():
    S = input()
    P = input()

    s = deque(S)
    n = len(S)
    for _ in range(n):
        s.append(s.popleft())
        if P in ''.join(s):
            ans = 'Yes'
            break
    else:
        ans = 'No'

    print(ans)

main()