class Dice:
    """Dice class"""
    def __init__(self):                  # ?????????????????????
        self.eyeIndex = 1        #center
        self.eyeIndex_E = 3      #east
        self.eyeIndex_W = 4      #west
        self.eyeIndex_N = 5      #north
        self.eyeIndex_S = 2      #south
        self.eye = 0
        self.eye_S = 0
        self.eye_E = 0
        self.eyes = []

    def convEyesIndexToEyes(self):
        self.eye = self.eyes[self.eyeIndex]
        self.eye_S = self.eyes[self.eyeIndex_S]
        self.eye_E = self.eyes[self.eyeIndex_E]
 

    def shakeDice(self, in_command):
        pre_eyeIndex = self.eyeIndex
        if in_command == "E":
            self.eyeIndex = self.eyeIndex_W 
            self.eyeIndex_E = pre_eyeIndex 
            self.eyeIndex_W = 7 - self.eyeIndex_E
            
        elif in_command == "W":
            self.eyeIndex = self.eyeIndex_E 
            self.eyeIndex_W = pre_eyeIndex
            self.eyeIndex_E = 7 - self.eyeIndex_W
            
        elif in_command == "N":
            self.eyeIndex = self.eyeIndex_S 
            self.eyeIndex_N = pre_eyeIndex 
            self.eyeIndex_S = 7 - self.eyeIndex_N

        elif in_command == "S":
            self.eyeIndex = self.eyeIndex_N         
            self.eyeIndex_S = pre_eyeIndex 
            self.eyeIndex_N = 7 - self.eyeIndex_S 
        
        self.convEyesIndexToEyes()


    def rotateDice(self):
        #rotate clockwise
        pre_E = self.eyeIndex_E
        pre_S = self.eyeIndex_S
        pre_W = self.eyeIndex_W
        pre_N = self.eyeIndex_N
        
        self.eyeIndex_E = pre_N
        self.eyeIndex_S = pre_E
        self.eyeIndex_W = pre_S
        self.eyeIndex_N = pre_W

        self.convEyesIndexToEyes()
        
    def getEye(self):
        return self.eye
        
    def getEye_S(self):
        return self.eye_S
    
    def getEye_E(self):
        return self.eye_E

    def setEyes(self, eyes):             # setEyes()???????????? ???????????????
        eyes = "0 " + eyes
        self.eyes = list(map(int, eyes.split(" ")))
        self.convEyesIndexToEyes()
        
dice_1 = Dice()
dice_1.setEyes(input().rstrip())
command_time = int(input().rstrip())

for i in range(command_time):
    in_eye, in_eye_S = map(int, input().rstrip().split(" "))
    
    shake_direction = "E"
    def_eye = dice_1.getEye()
    
    while True:
        dice_1.shakeDice(shake_direction)

        if dice_1.getEye() == in_eye:
            break
        if dice_1.getEye() == def_eye:
            shake_direction = "N"

    while True:
        if dice_1.getEye_S() == in_eye_S:
            break
        dice_1.rotateDice()


    print(dice_1.getEye_E())