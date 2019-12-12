# Attempting to rebuild the IntCode computer with class declarations and methods
# Should be a complete refactoring or reconstruction of the IntCode computer used in days 2, 5, and 7.

# This class stores a state for the memory, the ram, and the pointer's current address.
class IntCode():
    """A class to handle intcode computations."""

    def __init__(self, identifier, memoryTable=[], ramStack=[], pointerAddress=0, relativeBase=0, active=0):
        self.id = identifier
        self.mem = memoryTable.copy()
        self.ram = ramStack
        self.pointerAddress = pointerAddress
        self.base = relativeBase
        self.active = active

    def displayState(self):
        print("ID: " + self.id)
        print("Opcode: " + self.mem[self.pointerAddress])
        print("RAM: ")
        print(self.ram)
        print("Pointer: " + str(self.pointerAddress))
        print("Base " + str(self.base))
        print("Active " + str(self.active))

    def incrementPointer(self, increment: int) -> None:
        self.pointerAddress += increment

    def setPointer(self, address=0):
        self.pointerAddress = address

    def loadMemory(self, memory):
        self.mem = memory

    def readRam(self):
        return self.ram.pop(0)

    def writeRam(self, value):
        self.ram.insert(0, value)

    def getMem(self, index):
        try:
            x = self.mem[index]
            return x
        except IndexError:
            self.mem = self.mem + ([0] * (index + 1 - len(self.mem)))
            y = self.mem[index]
            return y
        except:
            print("Error retrieving memory at address: " + str(index) + ".")
            displayState()
            exit()

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
            result = [self.readRam() for x in range(0,len(self.ram))]
            result.reverse()
            self.active = 0
            print(result)
            return result

        # Process scope of 3 other values for later handling
        first = self.getMem(self.pointerAddress + 1)
        second = self.getMem(self.pointerAddress + 2)
        third = self.getMem(self.pointerAddress + 3)

        # Main if/elif block to handle and process code segment
        if instruction == 1:
            x = self.getMem(third)
            y = self.getMem(third + self.base)
            if mode3 == 0:
                self.mem[third] = (self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first) + (self.getMem(second) if mode2 == 0 else self.getMem(second + self.base) if mode2 == 2 else second)
            elif mode3 == 2:
                self.mem[third + self.base] = (self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first) + (self.getMem(second) if mode2 == 0 else self.getMem(second + self.base) if mode2 == 2 else second)
            self.incrementPointer(4)
        elif instruction == 2:
            x = self.getMem(third)
            y = self.getMem(third + self.base)
            if mode3 == 0:
                self.mem[third] = (self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first) * (self.getMem(second) if mode2 == 0 else self.getMem(second + self.base) if mode2 == 2 else second)
            elif mode3 == 2:
                self.mem[third + self.base] = (self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first) * (self.getMem(second) if mode2 == 0 else self.getMem(second + self.base) if mode2 == 2 else second)
            self.incrementPointer(4)
        elif instruction == 3:
            if not self.ram:
                self.active = 0
                print("Halting process: Awaiting next input signal.")
            else:
                value = self.readRam()
                x = self.getMem(first)
                if mode1 == 0:
                    self.mem[first] = value
                elif mode1 == 2:
                    self.mem[first + self.base] = value
                self.incrementPointer(2)
        elif instruction == 4:
            x = self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first
            self.writeRam(x)
            self.incrementPointer(2)
        elif instruction == 5:
            if (self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first) != 0:
                x = self.getMem(second) if mode2 == 0 else self.getMem(second + self.base) if mode2 == 2 else second
                self.setPointer(x)
            else:
                self.incrementPointer(3)
        elif instruction == 6:
            if (self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first) == 0:
                x = self.getMem(second) if mode2 == 0 else self.getMem(second + self.base) if mode2 == 2 else second
                self.setPointer(x)
            else:
                self.incrementPointer(3)
        elif instruction == 7:
            if (self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first) < (self.getMem(second) if mode2 == 0 else self.getMem(second + self.base) if mode2 == 2 else second):
                x = self.getMem(third)
                if mode3 == 0:
                    self.mem[third] = 1
                elif mode3 == 2:
                    self.mem[third + self.base] = 1
            else:
                x = self.getMem(third)
                if mode3 == 0:
                    self.mem[third] = 0
                elif mode3 == 2:
                    self.mem[third + self.base] = 0
            self.incrementPointer(4)
        elif instruction == 8:
            if (self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first) == (self.getMem(second) if mode2 == 0 else self.getMem(second + self.base) if mode2 == 2 else second):
                x = self.getMem(third)
                if mode3 == 0:
                    self.mem[third] = 1
                elif mode3 == 2:
                    self.mem[third + self.base] = 1
            else:
                x = self.getMem(third)
                if mode3 == 0:
                    self.mem[third] = 0
                elif mode3 == 2:
                    self.mem[third + self.base] = 0
            self.incrementPointer(4)
        elif instruction == 9:
            x = self.getMem(first) if mode1 == 0 else self.getMem(first + self.base) if mode1 == 2 else first
            self.base += x
            self.incrementPointer(2)
        else:
            print("Opcode error: INVALID INSTRUCTION")
            print("Opcode: " + str(instruction))
            displayState()
            return

    def executeIntCode(self):
        self.active = 1
        while self.active == 1:
            self.executeOpcode()
