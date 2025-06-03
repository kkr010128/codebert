
import glob

# 問題ごとのディレクトリのトップからの相対パス
REL_PATH = 'ABC\\169\\E'

# テスト用ファイル置き場のトップ
TOP_PATH = 'C:\\AtCoder'


class Common:
    problem = []
    index = 0

    def __init__(self, rel_path):
        self.rel_path = rel_path

    def initialize(self, path):
        file = open(path)
        self.problem = file.readlines()
        self.index = 0
        return

    def input_data(self):
        try:
            IS_TEST
            self.index += 1
            return self.problem[self.index - 1]

        except NameError:
            return input()

    def resolve(self):
        pass

    def exec_resolve(self):
        try:
            IS_TEST
            for path in glob.glob(TOP_PATH + '\\' + self.rel_path + '/*.txt'):
                print("Test: " + path)
                self.initialize(path)
                self.resolve()
                print("\n\n")
        except NameError:
            self.resolve()


class Solver(Common):

    def resolve(self):

        N = int(self.input_data())
        A = [[0, 0] for i in range(N)]
        B = [[0, 0] for i in range(N)]

        for i in range(N):
            tmp = self.input_data().split()
            A[i][0] = i
            A[i][1] = int(tmp[0])
            B[i][0] = i
            B[i][1] = int(tmp[1])

        # 最小値群と最大値群を個別に並び替える
        A_sorted = sorted(A, key=lambda x: x[1])
        B_sorted = sorted(B, key=lambda x: x[1])
        '''
        if N % 2 == 0:
            for i in range(N):
                for j in range(N):
                    if A_sorted[j][0] == i:
                        min = A_sorted[j]
                        break
                for j in range(N):
                    if B_sorted[j][0] == i:
                        max = B_sorted[j]
                        break
                

            pass
        else:
            pass
        '''
        if N % 2 == 0:
            median_min = A_sorted[int(N/2)][1] + A_sorted[int(N/2)-1][1]
            median_max = B_sorted[int(N/2)][1] + B_sorted[int(N/2)-1][1]
        else:
            median_min = A_sorted[int(N/2)][1]
            median_max = B_sorted[int(N/2)][1]
        result = median_max - median_min + 1

        print(str(result))



solver = Solver(REL_PATH)
solver.exec_resolve()
