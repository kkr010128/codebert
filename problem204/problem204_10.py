import sys
import collections
import itertools


def resolve(in_):
    one = ord(b'1')
    two = ord(b'2')
    # print(f'{one=} {two=}')

    S = in_.readline().strip()
    q = collections.deque(S)
    # print(f'{S=} {q=}')

    reverse_flag = False
    Q = int(in_.readline())
    for query in itertools.islice(in_, Q):
        T = query[0]
        if T == one:
            reverse_flag ^= True 
            # q.reverse()
        elif T == two:
            F = query[2]
            C = query[4]
            if (F == one) ^ reverse_flag:
                q.appendleft(C)
            else:
                q.append(C)
    else:
        if reverse_flag:
            q.reverse()
            reverse_flag = 0

    return bytes(q)


def main():
    answer = resolve(sys.stdin.buffer)
    print(answer.decode('ascii'))


if __name__ == '__main__':
    main()
