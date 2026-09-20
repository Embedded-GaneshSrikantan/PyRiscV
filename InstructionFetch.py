# this fetches the instruction from memory and sends it to the instruction decode 

from Memory import Memory

class InstructionFetch():
    def __init__(self):
        self.memory = Memory().create_memory(1024)  # Initialize memory with a size of 1024 bytes
        self.pc = 0  # Program counter initialized to 0
        self.instruction = None

    def fetch(self):
        self.instruction = self.memory.read(self.pc)
        self.pc += 4  # Increment program counter by 4 for the next instruction
        return self.instruction
        