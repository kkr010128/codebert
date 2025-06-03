if __name__ == '__main__':
    try:
        n = int(raw_input())
    except:
        print 'the first input must be integer value!'
        exit()

    genoms = set([])
    answers = []
    for _ in range(n):
        values = raw_input().split()
        order = values[0]
        genom = values[1]
        if order == "insert":
            genoms.add(genom)
        else:
            # TODO: fasten here!
            answers.append('yes' if genom in genoms else 'no' )

    # print(genoms)
    # print(answers)

    for answer in answers:
        print answer