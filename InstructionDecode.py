#this file contains all the decoding logic for the riscv instructions that are currently supported by the emulator

from unittest import result

from InstructionExecute import InstExecuteRV


class InstructionDecode():
    def __init__(self):
        self.instruction = None
        self.opcode = None
        self.funct3 = None
        self.funct7 = None
        self.rs1 = 0
        self.rs2 = 0
        self.immediate1 = 0
        self.immediate2 = 0
        self.rd = 0

    def decode(self, instruction):
        self.instruction = instruction
        self.getOpCode()
        self.sendToExecute()

    def getOpCode(self):
        self.opcode = self.instruction & 0x7F
        if self.opcode == 0x33:  # R-type
            self.getRTypeFields()
        elif self.opcode == 0x13:  # I-type
            self.getITypeFields()
        elif self.opcode == 0x3:   # Load (I-type)
            self.getITypeFields()
        elif self.opcode == 0x23:  # S-type
            self.getSTypeFields()
        elif self.opcode == 0x63:  # B-type
            self.getBTypeFields()
        elif self.opcode == 0x37:  # U-type (LUI)
            self.getUTypeFields()
        elif self.opcode == 0x17:  # U-type (AUIPC)
            self.getUTypeFields()
        elif self.opcode == 0x6F:  # J-type (JAL)
            self.getJTypeFields()
        else:
            print("Unsupported opcode:", hex(self.opcode))

    def getRTypeFields(self):
        self.rd = (self.instruction >> 7) & 0x1F
        self.funct3 = (self.instruction >> 12) & 0x7
        self.rs1 = (self.instruction >> 15) & 0x1F
        self.rs2 = (self.instruction >> 20) & 0x1F
        self.funct7 = (self.instruction >> 25) & 0x7F
        self.immediate1 = 0
        self.immediate2 = 0 

    def getITypeFields(self):
        self.rd = (self.instruction >> 7) & 0x1F
        self.funct3 = (self.instruction >> 12) & 0x7
        self.rs1 = (self.instruction >> 15) & 0x1F
        self.immediate1 = (self.instruction >> 20) & 0xFFF
        self.rs2 = 0
        self.funct7 = 0
        self.immediate2 = 0

    def getSTypeFields(self):
        self.immediate1 = (self.instruction & 0xFE000000 ) >> 25 
        self.funct3 = (self.instruction >> 12) & 0x7
        self.rs2 = (self.instruction >> 20) & 0x1F
        self.rs1 = (self.instruction >> 15) & 0x1F
        self.rd = 0
        self.funct7 = 0
        self.immediate2 = (self.instruction & 0x00000F80) >> 7 # for instructions like beq where two sets of 
                            #immediate values are used,
                            #  we can store the second set in this variable

    def getBTypeFields(self):
        self.immediate1 = (self.instruction >> 25 ) & 0x7F
        self.immediate2 = (self.instruction >> 7) & 0x1F
        self.funct3 = (self.instruction >> 12) & 0x7
        self.rs2 = (self.instruction >> 20) & 0x1F
        self.rs1 = (self.instruction >> 15) & 0x1F
        self.rd = 0
        self.funct7 = 0
        

    def getUTypeFields(self):
        self.rd = (self.instruction >> 7) & 0x1F
        self.immediate1 = (self.instruction >> 12) & 0xFFFFF
        self.funct3 = 0
        self.rs1 = 0
        self.rs2 = 0
        self.funct7 = 0
        self.immediate2 = 0 # for instructions like beq where two sets of

    def getJTypeFields(self):
        self.immediate = ((self.instruction >> 31) & 0x1) << 20 | ((self.instruction >> 21) & 0x3FF) << 1 | ((self.instruction >> 20) & 0x1) << 11 | (self.instruction >> 12) & 0x7FF
        self.rd = (self.instruction >> 7) & 0x1F
        self.funct3 = 0
        self.rs1 = 0
        self.rs2 = 0
        self.funct7 = 0
        self.immediate2 = 0 

    def sendToExecute(self):
        executor = InstExecuteRV()
        executor.opcode = self.getInstructionName()
        executor.a = self.rs1
        executor.b = self.rs2 if self.rs2 != 0 else self.immediate1
        result = executor.execute()
        print(f"Executed {executor.opcode} with a={executor.a}, b={executor.b}, result={result}")