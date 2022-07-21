from DeviceDriver import Driver
from UDPClient import Client
from CursorPointer import Pointer

class Main:
    def __init__(self):
        self.udp = Client().initClient()
        self.driver = Driver(self.udp)
        self.pointer = Pointer(self.driver)

    def testFunction(self):
        while(True):
            self.pointer.getInstruction()



ob = Main()
ob.testFunction()