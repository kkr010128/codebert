class dice:
    def __init__(self,A):
        self.side = {
            "TOP":A[0],
            "S":A[1],
            "E":A[2],
            "W":A[3],
            "N":A[4],
            "BOT":A[5],
            }
        self.reverse = {
            "E":"W",
            "W":"E",
            "S":"N",
            "N":"S"}
        
    def main(self,A):
        for s in A:
            var = int(self.side[s])
            self.side[s] = self.side["TOP"]
            self.side["TOP"] = self.side[self.reverse[s]]
            self.side[self.reverse[s]] = self.side["BOT"]
            self.side["BOT"] = var
        print("{}".format(self.side["TOP"]))

var = dice(list(map(int,input().split())))
var.main(input())
