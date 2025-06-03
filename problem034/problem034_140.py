
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
    
    def right_rotation(self):
        reg = self.label2
        self.label2 = self.label3
        self.label3 = self.label5
        self.label5 = self.label4
        self.label4 = reg
    

    def search(self, value):
        while True :
            self.N_rotation()
            if value[0] == self.label1:
                break
            self.E_rotation()
            if value[0] == self.label1:
                break
            
        while True :
            self.right_rotation()
            if value[1] == self.label2:
                break
            
init_dise = input().split()
times = int(input())

for i in range(times):
    dise1 = dise(init_dise)
    order = input().split()
    dise1.search(order)
    print(dise1.label3)