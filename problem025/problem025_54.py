def create_sums(ns):
    if len(ns) == 0:
        return set()

    s = create_sums(ns[1:])
    return {e + ns[0] for e in s} | s | {ns[0]}


def run_set():
    _ = int(input())  # flake8: noqa
    ns = [int(i) for i in input().split()]

    sums = create_sums(ns)
    _ = int(input())  # flake8: noqa

    for q in (int(j) for j in input().split()):
        if q in sums:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    run_set()


