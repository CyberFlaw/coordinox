from concurrent.futures import thread
from DeviceDriver import Driver
from UDPClient import Client
from CursorPointer import Pointer

import threading
import sys

# Check ip 
class Main(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.udp = Client("192.168.137.19", 4210).initClient()
        self.driver = Driver(self.udp)
        self.pointer = Pointer(self.driver)

    def run(self):
        while(True):
            self.pointer.getInstruction()
            queue = self.pointer.getInstructionQueue()
            if (queue != []):
                self.pointer.moveCursor()
         
thread1 = Main()
thread1.daemon = True
thread1.start()

while True:
    if input() == "quit":
        sys.exit()
