class Dice(object):

    def __init__(self, num):
        self.num = num

    def rotate_S(self):
        self.num = [self.num[4], self.num[0], self.num[2], self.num[3], self.num[5], self.num[1]]

    def rotate_N(self):
        self.num = [self.num[1], self.num[5], self.num[2], self.num[3], self.num[0], self.num[4]]

    def rotate_W(self):
        self.num = [self.num[2], self.num[1], self.num[5], self.num[0], self.num[4], self.num[3]]

    def rotate_E(self):
        self.num = [self.num[3], self.num[1], self.num[0], self.num[5], self.num[4], self.num[2]]

    def get_right_num(self, a, b):
        top_index = self.num.index(a) + 1
        front_index = self.num.index(b) + 1
        if [top_index, front_index] in [[2, 3], [3, 5], [5, 4], [4, 2]]:
            return self.num[0]
        elif [top_index, front_index] in [[1, 4], [4, 6], [6, 3], [3, 1]]:
            return self.num[1]
        elif [top_index, front_index] in [[1, 2], [2, 6], [6, 5], [5, 1]]:
            return self.num[2]
        elif [top_index, front_index] in [[1, 5], [5, 6], [6, 2], [2, 1]]:
            return self.num[3]
        elif [top_index, front_index] in [[1, 3], [3, 6], [6, 4], [4, 1]]:
            return self.num[4]
        elif [top_index, front_index] in [[2, 4], [4, 5], [5, 3], [3, 2]]:
            return self.num[5]

dice = Dice(map(int, raw_input().split()))
Q = input()
for q in range(Q):
    num_set = map(int, raw_input().split())
    print dice.get_right_num(num_set[0], num_set[1])