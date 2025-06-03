from collections import deque
k = int(input())
q = deque()
def main():
    for i in range(1, 10):
        q.append(i)
    for _ in range(k):
        x = q.popleft()
        if x % 10 != 0:
            q.append(x * 10 + x%10 - 1)
        q.append(x * 10 + x%10)
        if x % 10 != 9:
            q.append(x * 10 + x%10 + 1)
    print(x)

        
if __name__ == '__main__':
    main()