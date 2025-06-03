from collections import deque

def run():
    n = int(input())
    dq = deque()
    for _ in range(n):
        order = input()
        if order[0] == 'i':
            dq.appendleft(order[7:])
        elif order[6] == ' ':
            key = order.split()[1]
            if not key in dq:
                continue
            for i in range(len(dq)):
                if dq[i] == key:
                    dq.remove(key)
                    break
        elif order[6] == 'F':
            dq.popleft()
        elif order[6] == 'L':
            dq.pop()

    print(' '.join(dq))

if __name__ == '__main__':
    run()


