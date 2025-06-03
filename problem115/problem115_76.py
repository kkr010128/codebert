""" Atcorder practice 20200719 """
# test programm for practice


def __main__():
    """ def for calc """
    num_input = int(input())
    if num_input < 1 or num_input > 10:
        raise ValueError
    #elif num_input % 1 != 0:
        #raise ValueError
    else:
        print(num_input + num_input**2 + num_input**3)


if __name__ == "__main__":
    __main__()
