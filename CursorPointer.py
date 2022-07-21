import pyautogui

class Pointer:
    def __init__(self, driver):     
        self.driver = driver
        self.projetionDimentions = self.driver.getProjectionDimentions()        # Width - 0, Height - 1
        self.screenDimentions = [34.5, 19.6]                                    # Width - 0, Height - 1
        self.scaleFactors = [self.projetionDimentions[0] / self.screenDimentions[0], self.projetionDimentions[1] / self.screenDimentions[1]]    # x - 0, y - 1    projection/screen
        self.instructionQueue = []

    def __getScaledInstrucion(self, instruction):
        xRaw = int(instruction.split(',')[0].split(':')[1][1:])
        yRaw = int(instruction.split(',')[1])

        xScale = xRaw / self.scaleFactors[0]
        yScale = yRaw / self.scaleFactors[1]

        print("x: ", xScale, ", y: ", yScale)
        # new = instruction.split(':')[0] + ": " + xScale + ", ", yScale
        # print(new)

        # return new


    def getInstruction(self):
        instruction = self.driver.getInstruction()
        print("Scale factors: ", self.scaleFactors)
        print("Projection: ", self.projetionDimentions)
        
        match instruction.split(':')[0]:
            case 'cx':
                self.driver.setCalibration(instruction)
            
            case 'cy':
                self.driver.setCalibration(instruction)
            
            # case 'move':
            #     self.instructionQueue.append(self.__getScaledInstrucion())
            
            case 'click':
                self.__getScaledInstrucion(instruction)
                # print(self.instructionQueue)

    

            