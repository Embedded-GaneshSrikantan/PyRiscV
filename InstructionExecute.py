#THIS FILE IS INSTRUCTION EXECUTION 


class InstExecuteRV():
    
    def __init__(self):
        
        self.opcode = None
        self.a           = 0
        self.b           = 0
        self.result      = 0 
        
    
    def execute(self): 
        if self.opcode == "ADD":
            self.result = self.a + self.b
        elif self.opcode == "SUB":
            self.result = self.a - self.b
        elif self.opcode == "AND":
            self.result = self.a & self.b
        elif self.opcode == "OR":
            self.result = self.a | self.b
        else:
            print("Invalid Instruction")
        
        return self.result