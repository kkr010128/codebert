
class dise:
    def __init__(self, label):
        self.label1 = label[0]
        self.label2 = label[1]
        self.label3 = label[2]
        self.label4 = label[3]
        self.label5 = label[4]
        self.label6 = label[5]
    
    def N_rotation(self):
        reg = self.label1
        self.label1 = self.label2
        self.label2 = self.label6
        self.label6 = self.label5
        self.label5 = reg
        
    def E_rotation(self):
        reg = self.label1
        self.label1 = self.label4
        self.label4 = self.label6
        self.label6 = self.label3
        self.label3 = reg
        
    def S_rotation(self):
        reg = self.label1
        self.label1 = self.label5
        self.label5 = self.label6
        self.label6 = self.label2
        self.label2 = reg
        
    def W_rotation(self):
        reg = self.label1
        self.label1 = self.label3
        self.label3 = self.label6
        self.label6 = self.label4
        self.label4 = reg

dise1 = dise(input().split())
order = list(input())

for i in order:
    if i == 'N':
        dise1.N_rotation()
    elif i == 'E':
        dise1.E_rotation()
    elif i == 'S':
        dise1.S_rotation()
    elif i == 'W':
        dise1.W_rotation()

print(dise1.label1)