from DeviceDriver import Driver
from UDPClient import Client
from CursorPointer import Pointer

# Check ip 
class Main:
    def __init__(self):
        self.udp = Client("192.168.137.19", 4210).initClient()
        self.driver = Driver(self.udp)
        self.pointer = Pointer(self.driver)

    def testFunction(self):
        while(True):
            self.pointer.getInstruction()
            queue = self.pointer.getInstructionQueue()
            if (queue != []):
                self.pointer.moveCursor()

ob = Main()
ob.testFunction()