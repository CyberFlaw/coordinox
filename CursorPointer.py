from tkinter import Scale
import pyautogui

class Pointer:
    def __init__(self, driver):     
        self.driver = driver
        self.projetionDimentions = [0, 0]      # Width - 0, Height - 1
        self.screenDimentions = [34.5, 19.6]                                    # Width - 0, Height - 1
        self.scaleFactors = [1, 1]    # x - 0, y - 1    projection/screen
        self.instructionQueue = []

    def __setScalingFactors(self):
        self.projetionDimentions = self.driver.getProjectionDimentions() 
        self.scaleFactors = [self.projetionDimentions[0] / self.screenDimentions[0], self.projetionDimentions[1] / self.screenDimentions[1]]

    def __getWindowScaledInstruction(self, x, y):
        screen_width, screen_height = pyautogui.size()
        scaleFactorX = screen_width / x
        scaleFactorY = screen_height / y

        return (x * scaleFactorX, y * scaleFactorY)

    def __getScaledInstrucion(self, instruction):
        xRaw = int(instruction.split(',')[0].split(':')[1][1:])
        yRaw = int(instruction.split(',')[1])

        xCalib = self.driver.getXCalibration()
        yCalib = self.driver.getYCalibration()

        x = xCalib[0] - xRaw
        y = yRaw - yCalib[1]

        xScale = int(x / self.scaleFactors[0])
        yScale = int(y / self.scaleFactors[1])
        print("x: ", xScale, ", y: ", yScale)

        xWindowScale, yWindowScale = self.__getWindowScaledInstruction(xScale, yScale)

        return instruction.split(':')[0] + ": " + "% s" % xWindowScale + ", " +"% s" % yWindowScale

    def getInstruction(self):
        instruction = self.driver.getInstruction()
        # print("Scale factors: ", self.scaleFactors)
        # print("Projection: ", self.projetionDimentions)
        
        match instruction.split(':')[0]:
            case 'cx':
                self.driver.setCalibration(instruction)
                self.__setScalingFactors()
            
            case 'cy':
                self.driver.setCalibration(instruction)
                self.__setScalingFactors()
            # case 'move':
            #     self.instructionQueue.append(self.__getScaledInstrucion())
            
            case 'click':
                self.__getScaledInstrucion(instruction)
                # print(self.instructionQueue)

    

            