## registerfile

## this contains the register class for the riscV architecture 

class RegisterFile():
    def __init__(self):
        self.registers = { "x0": 0, "x1": 0,\
                         "x2": 0, "x3": 0, "x4": 0,\
                         "x5": 0, "x6": 0,\
                         "x7": 0, "x8": 0,\
                         "x9": 0, "x10": 0,\
                         "x11": 0, "x12": 0,\
                         "x13": 0, "x14": 0,\
                         "x15": 0, "x16": 0,\
                         "x17": 0, "x18": 0,\
                         "x19": 0, "x20": 0,\
                         "x21": 0, "x22": 0,\
                         "x23": 0, "x24": 0,\
                         "x25": 0, "x26": 0,\
                         "x27": 0, "x28": 0,\
                         "x29": 0, "x30": 0,\
                         "x31": 0,"pc": 0}

    def read(self, reg):
        for i in range(32):
            if reg == i:
                return self.registers[f"x{i}"]
        else:
            raise ValueError("Register number must be between 0 and 31")

    def write(self, reg, value):
        if reg == "pc":
            self.registers["pc"] = value
            return
        for i in range(32):
            if reg == 0:
                print("Cannot write to x0 register. It is always 0.")
                return
            elif reg == i:
                self.registers[f"x{i}"] = value
                return
            
            else:
                continue
        
        else:
            raise ValueError("Register number must be between 0 and 31")