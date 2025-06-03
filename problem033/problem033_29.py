class dice:
    value = [0] * 6
    def __init__(self, list):
        self.value = list

    def dice_roll(self,dir):
        if dir == "S":
            prev = self.value
            self.value = [prev[4],prev[0],prev[2],prev[3],prev[5],prev[1]]
        elif dir == "N":
            prev = self.value
            self.value = [prev[1],prev[5],prev[2],prev[3],prev[0],prev[4]]
        elif dir == "W":
            prev = self.value
            self.value = [prev[2],prev[1],prev[5],prev[0],prev[4],prev[3]]
        elif dir == "E":
            prev = self.value
            self.value = [prev[3],prev[1],prev[0],prev[5],prev[4],prev[2]]

mydice = dice(list(map(int, input().split())))
x = str(input())
for i in x:
    mydice.dice_roll(i)
print(mydice.value[0])
