from math import floor
from tkinter import Scale
import pyautogui

class Pointer:
    def __init__(self, driver):     
        self.driver = driver
        self.projetionDimentions = [0, 0]      # Width - 0, Height - 1
        self.scaleFactors = [1, 1]    # x - 0, y - 1    screen/projection
        self.instructionQueue = []
        self.screen_width, self.screen_height = pyautogui.size()

    def getInstructionQueue(self):
        return self.instructionQueue

    def __setScalingFactors(self):
        self.projetionDimentions = self.driver.getProjectionDimentions() 
        self.scaleFactors = [self.projetionDimentions[0] / self.screen_width, self.projetionDimentions[1] / self.screen_height]

    def __getScaledInstrucion(self, instruction):
        xRaw = int(instruction.split(',')[0].split(':')[1][1:])
        yRaw = int(instruction.split(',')[1])

        xCalib = self.driver.getXCalibration()
        yCalib = self.driver.getYCalibration()

        x = xCalib[0] - xRaw
        y = yCalib[1] - yRaw

        xScale = int(x / self.scaleFactors[0])
        yScale = abs(int(y / self.scaleFactors[1]))

        return instruction.split(':')[0] + ": " + "% s" % xScale + ", " +"% s" % yScale

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
            #     self.instructionQueue.append(self.__getScaledInstrucion(instruction))
            
            case 'click':
                self.instructionQueue.append(self.__getScaledInstrucion(instruction))
                # print(self.instructionQueue)

    def moveCursor(self):
        instruction = self.instructionQueue.pop()
        print(instruction)
        # Change to move
        # if(int(instruction.split(',')[0].split(':')[1][1:]) > 0 and int(instruction.split(',')[1]) > 0):
        #     if(instruction.split(':')[0] == 'click'):
        
        x = int(instruction.split(',')[0].split(':')[1][1:])
        y = int(instruction.split(',')[1])

        pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
    

            