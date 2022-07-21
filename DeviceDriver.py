class Driver:
    def __init__(self, client):
        self.udp = client
        self.projectionDimentions = [0, 0]          # width - 0, height - 1
        self.topLeftCoordinates = [0, 0]
        self.bottomRightCoordinates = [0, 0]
        self.bufferSize = 32

    def getInstruction(self):
        payload = self.udp.recvfrom(self.bufferSize)
        instruction = format(payload[0])[2:-1]
        return instruction
        
    def getProjectionDimentions(self):
        return self.projectionDimentions;

    def setCalibration(self, instruction):
        if ((self.topLeftCoordinates[0] != 0 and self.bottomRightCoordinates[0] != 0) and self.projectionDimentions[0] == 0 ):
            self.projectionDimentions[0] = self.topLeftCoordinates[0] - self.bottomRightCoordinates[0]
            self.projectionDimentions[1] = self.bottomRightCoordinates[1] - self.topLeftCoordinates[1]

        elif (self.projectionDimentions[1] != 0 and self.projectionDimentions[0] != 0):
            print("Already Calibrated!")

        else:
            if (instruction.split(":")[0] == 'cx'):
                self.topLeftCoordinates[0] = int(instruction.split(',')[0].split(':')[1][1:])
                self.topLeftCoordinates[1] = int(instruction.split(',')[1])
                print("X coordinate calibrated")

            elif (instruction.split(":")[0] == 'cy'):
                self.bottomRightCoordinates[0] = int(instruction.split(',')[0].split(':')[1][1:])
                self.bottomRightCoordinates[1] = int(instruction.split(',')[1][1:])
                print("Y coordinate calibrated")
                    


