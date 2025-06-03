from itertools import chain

def main():
    inputs = []
    r, _ = map(int, input().split())
    for i in range(r):
        inputs.append(tuple(map(int, input().split())))

    row_sums = map(lambda row: sum(row), inputs)
    column_sums = map(lambda column: sum(column), map(lambda *x: x, *inputs))
    all_sum = sum(chain.from_iterable(inputs))

    for i, s in zip(inputs, row_sums):
        print(" ".join(map(lambda n: str(n), i)) + " {}".format(s))
    else:
        print(" ".join(map(lambda n: str(n), column_sums)) + " {}".format(all_sum))

if __name__ == "__main__":
    main()