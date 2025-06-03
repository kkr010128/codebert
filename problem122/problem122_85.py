import collections

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    a_dict = collections.Counter(a)
    a_dict = {key: key*value for key, value in a_dict.items()}
    answer = sum(a_dict.values())
    for _ in range(q):
        b, c = map(int, input().split())
        diff = 0
        if b in a_dict:
            b_sum = a_dict.pop(b)
            c_add = b_sum//b * c
            diff = c_add - b_sum
            if c in a_dict:
                a_dict[c] += c_add
            else:
                a_dict[c] = c_add
        answer += diff
        print(answer)


if __name__ == '__main__':
    main()
