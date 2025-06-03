
class Dise():
    def __init__(self, aLabelList):
        self.LabelList = aLabelList
        self.LabelsRelationship = [[0 for i in range(5)] for j in range(6)]
        for i in range(6):
            if i == 0:
                self.LabelsRelationship[i][0] = self.LabelList[2 -1] #下1
                self.LabelsRelationship[i][1] = self.LabelList[3 -1] #下2
                self.LabelsRelationship[i][2] = self.LabelList[5 -1] #下3
                self.LabelsRelationship[i][3] = self.LabelList[4 -1] #下4
                self.LabelsRelationship[i][4] = self.LabelList[6 -1] #対面
            elif i == 1:
                self.LabelsRelationship[i][0] = self.LabelList[6 -1] #下1
                self.LabelsRelationship[i][1] = self.LabelList[3 -1] #下2
                self.LabelsRelationship[i][2] = self.LabelList[1 -1] #下3
                self.LabelsRelationship[i][3] = self.LabelList[4 -1] #下4
                self.LabelsRelationship[i][4] = self.LabelList[5 -1] #対面
            elif i == 2:
                self.LabelsRelationship[i][0] = self.LabelList[6 -1] #下1
                self.LabelsRelationship[i][1] = self.LabelList[5 -1] #下2
                self.LabelsRelationship[i][2] = self.LabelList[1 -1] #下3
                self.LabelsRelationship[i][3] = self.LabelList[2 -1] #下4
                self.LabelsRelationship[i][4] = self.LabelList[4 -1] #対面
            elif i == 3:
                self.LabelsRelationship[i][0] = self.LabelList[2 -1] #下1
                self.LabelsRelationship[i][1] = self.LabelList[1 -1] #下2
                self.LabelsRelationship[i][2] = self.LabelList[5 -1] #下3
                self.LabelsRelationship[i][3] = self.LabelList[6 -1] #下4
                self.LabelsRelationship[i][4] = self.LabelList[3 -1] #対面
            elif i == 4:
                self.LabelsRelationship[i][0] = self.LabelList[1 -1] #下1
                self.LabelsRelationship[i][1] = self.LabelList[3 -1] #下2
                self.LabelsRelationship[i][2] = self.LabelList[6 -1] #下3
                self.LabelsRelationship[i][3] = self.LabelList[4 -1] #下4
                self.LabelsRelationship[i][4] = self.LabelList[2 -1] #対面
            elif i == 5:
                self.LabelsRelationship[i][0] = self.LabelList[5 -1] #下1
                self.LabelsRelationship[i][1] = self.LabelList[3 -1] #下2
                self.LabelsRelationship[i][2] = self.LabelList[2 -1] #下3
                self.LabelsRelationship[i][3] = self.LabelList[4 -1] #下4
                self.LabelsRelationship[i][4] = self.LabelList[1 -1] #対面
            
    def DisePrintRight(self,aTopItem,aFront):
        xTopIndex = self.LabelList.index(str(aTopItem))
        for i in range(4):
            if int(self.LabelsRelationship[xTopIndex][i]) == aFront:
                if i + 1 == 4:
                    idxR = int(self.LabelsRelationship[xTopIndex][0])
                else:
                    idxR = int(self.LabelsRelationship[xTopIndex][i+1])
                print(idxR)
                break


myInstance = Dise(input().split())
 
x = int(input())
for i in range(x):
    a,b = map(int, input().split())
    myInstance.DisePrintRight(a,b)
    
