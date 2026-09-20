# This file contains all the riscv instructions that are currently supported by the emulator
# This file is referenced by instruction decode 


class RVInstructionSet():
    
    def __init__(self):
        
        self.instructionSet = ["ADD","SUB","AND","OR","ADDI"]