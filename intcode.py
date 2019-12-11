# Attempting to rebuild the IntCode computer with class declarations and methods
# Should be a complete refactoring or reconstruction of the IntCode computer used in days 2, 5, and 7.

# This class stores a state for the memory, the ram, and the pointer's current address.
class IntCode():
    """A class to handle intcode computations."""

    def __init__(self, identifier, memoryTable=[], ramStack=[], pointerAddress=0, active=0):
        self.id = identifier
        self.mem = memoryTable.copy()
        self.ram = ramStack
        self.pointerAddress = pointerAddress
        self.active = active

    def incrementPointer(self, increment: int) -> None:
        self.pointerAddress += increment

    def setPointer(self, address=0):
        self.pointerAddress = address

    def loadMemory(self, memory):
        self.mem = memory

    def readRam(self):
        return self.ram.pop()

    def writeRam(self, value):
        self.ram.append(value)

    def loadOpcode(self) -> list:
        opcode = str(self.mem[self.pointerAddress])
        mode1 = 0
        mode2 = 0
        mode3 = 0

        if len(opcode) > 1:
            instruction = int(opcode[-1]) + (int((opcode[-2])) * 10)
        else:
            instruction = int(opcode[-1])

        if len(opcode) > 2:
            mode1 = opcode[-3]
            if len(opcode) > 3:
                mode2 = opcode[-4]
                if len(opcode) > 4:
                    mode3 = opcode[-5]

        return [instruction, int(mode1), int(mode2), int(mode3)]

    def executeOpcode(self):
        opcode = self.loadOpcode()
        instruction = opcode[0]
        mode1 = opcode[1]
        mode2 = opcode[2]
        mode3 = opcode[3]

        if instruction == 99:
            result = self.mem[0]
            self.active = 0
            print(result)
            return result

        # Process scope of 3 other values for later handling
        first = self.mem[self.pointerAddress + 1]

        try:
            second = self.mem[self.pointerAddress + 2]
        except:
            second = 0

        try:
            third = self.mem[self.pointerAddress + 3]
        except:
            third = 0

        # Main if/elif block to handle and process code segment
        if instruction == 1:
            self.mem[third] = (self.mem[first] if mode1 == 0 else first) + (
                self.mem[second] if mode2 == 0 else second)
            self.incrementPointer(4)
        elif instruction == 2:
            self.mem[third] = (self.mem[first] if mode1 == 0 else first) * (self.mem[second] if mode2 == 0 else second)
            self.incrementPointer(4)
        elif instruction == 3:
            if not self.ram:
                self.active = 0
                #print("Halting process: Awaiting next input signal.")
            else:
                value = self.readRam()
                self.mem[first] = value
                self.incrementPointer(2)
        elif instruction == 4:
            x = self.mem[first] if mode1 == 0 else first
            self.writeRam(x)
            self.incrementPointer(2)
            self.active = 0
            return
        elif instruction == 5:
            if (self.mem[first] if mode1 == 0 else first) != 0:
                x = self.mem[second] if mode2 == 0 else second
                self.setPointer(x)
            else:
                self.incrementPointer(3)
        elif instruction == 6:
            if (code[first] if mode1 == 0 else first) == 0:
                x = self.mem[second] if mode2 == 0 else second
                self.setPointer(x)
            else:
                self.incrementPointer(3)
        elif instruction == 7:
            if (self.mem[first] if mode1 == 0 else first) < (self.mem[second] if mode2 == 0 else second):
                self.mem[third] = 1
            else:
                self.mem[third] = 0
            self.incrementPointer(4)
        elif instruction == 8:
            if (self.mem[first] if mode1 == 0 else first) == (self.mem[second] if mode2 == 0 else second):
                self.mem[third] = 1
            else:
                self.mem[third] = 0
            self.incrementPointer(4)
        else:
            print("Opcode error: INVALID INSTRUCTION")
            print("Opcode: " + str(instruction))

    def executeIntCode(self):
        self.active = 1
        while self.active == 1:
            self.executeOpcode()




# NOT IN USE
class Amplifier(IntCode):
    """A class declaration to handle amplifiers for Day 7."""

    def __init__(self, memoryTable=[], ramStack=[], pointerAddress=0, active=0, input=None, output=None):
        self.mem = memoryTable
        self.ram = ramStack
        self.pointerAddress = pointerAddress
        self.active = active
        self.input = input
        self.output = output

    def connectIn(self, prevAmp):
        self.input = prevAmp

    def connectOut(self, nextAmp):
        self.output = nextAmp

    def runAmp(self):
        self.executeIntCode()
