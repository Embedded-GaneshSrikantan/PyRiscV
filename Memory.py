# this simulates a flash or a storage device that can be read from and written to. 
# It is a simple implementation of a memory module for the RISC-V emulator.

class Memory():
    def __init__(self):
        self.size = 0
        self.memory = []
        

    def create_memory(self, size):
        self.size = size
        self.memory = [0] * size
        return self
    
    def read(self, address):
        if address < 0 or address >= self.size:
            raise ValueError("Address out of bounds")
            
        return self.memory[address]

    def write(self, address, value):
        if address < 0 or address >= self.size:
            raise ValueError("Address out of bounds")
        self.memory[address] = value
