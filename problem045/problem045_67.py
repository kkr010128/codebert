class ABProblem:
    def output(self, a, b):
        print "%d %d %.5f" % (a / b, a % b, a * 1.0 / b)

if __name__ == "__main__":
        abp = ABProblem()
        a, b = map(int, raw_input().split())
        abp.output(a, b)