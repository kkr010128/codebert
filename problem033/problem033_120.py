from sys import stdin

class Dice:
    def __init__(self, nums):
        self._1 = nums[0]
        self._2 = nums[1]
        self._3 = nums[2]
        self._4 = nums[3]
        self._5 = nums[4]
        self._6 = nums[5]
        self.pos = {
            "E" : self._3,
            "W" : self._4,
            "S" : self._2,
            "N" : self._5,
            "T" : self._1,
            "B" : self._6
        }

    def roll(self, query):
        for q in query:
            if q == "E":
                self.pos["T"], self.pos["E"], self.pos["B"], self.pos["W"] = self.pos["W"], self.pos["T"], self.pos["E"], self.pos["B"]
            elif q == "W":
                self.pos["T"], self.pos["E"], self.pos["B"], self.pos["W"] = self.pos["E"], self.pos["B"], self.pos["W"], self.pos["T"]
            elif q == "S":
                self.pos["T"], self.pos["S"], self.pos["B"], self.pos["N"] = self.pos["N"], self.pos["T"], self.pos["S"], self.pos["B"]
            elif q == "N":
                self.pos["T"], self.pos["S"], self.pos["B"], self.pos["N"] = self.pos["S"], self.pos["B"], self.pos["N"], self.pos["T"]

nums = [int(x) for x in stdin.readline().rstrip().split()]
queries = stdin.readline().rstrip()
d = Dice(nums)
d.roll(queries)
print(d.pos["T"])
