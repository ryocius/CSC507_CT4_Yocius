from random import randint


class MemoryContent:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getName(self):
        return self.name[:5]

    def getSize(self):
        return self.size

    def getSelf(self):
        return self.name[:5] + " size: " + str(self.size)


# Simulated 8 MB Memory Block
class MemoryBlock:
    def __init__(self, id):
        self.id = id[:5]
        self.maxCapacity = 8
        self.remainingCapacity = 8
        self.blockContents = []

    def allocateMemory(self, contents):
        if self.getRemainingCapacity() >= contents.getSize():
            self.remainingCapacity = self.remainingCapacity - contents.getSize()
            for i in range(contents.getSize()):
                self.blockContents.append(contents)
            print("Successfully allocated" + contents.getSelf() + " to memory block " + self.id)
            return True
        else:
            print("Failed to allocate" + contents.getSelf() + " to memory in memory block " + self.id)
            return False

    def getRemainingCapacity(self):
        return self.remainingCapacity

    def printBlock(self):
        mid = ""
        bottom = ""

        for i in range(len(self.blockContents)):
            bottom = bottom + self.blockContents[i].getName() + "\t"
        if len(self.blockContents) != 8:
            for j in range(8-len(self.blockContents)):
                bottom = bottom + "EMPTY\t"
        for k in range(8):
            mid = mid + str(k) + "    \t"

        top = "\t\t\t\t\t\t\t\t" +self.id + "\t\t\t\t\t\t\t\t"
        print("|" + top + "|" )
        print("|" + mid + "|" )
        print("|" + bottom + "|" )


# Simulated 64 MB of memory in 8 blocks
class Memory:
    def __init__(self):
        self.memory = []
        for i in range(8):
            self.memory.append(MemoryBlock(str(i)))

    def firstFitAllocate(self, contents):
        allocated = False
        i = 0
        while not allocated and i < len(self.memory):
            allocated = self.memory[i].allocateMemory(contents)
            i += 1


    def bestFitAllocate(self, contents):
        allocated = False
        i = 0
        while not allocated and i < len(self.memory):
            if self.memory[i].getRemainingCapacity() == contents.getSize():
                allocated = self.memory[i].allocateMemory(contents)
            i += 1

        if not allocated:
            self.firstFitAllocate(contents)

    def printMemory(self):
        for j in range(len(self.memory)):
            self.memory[j].printBlock()
        out = ""
        for k in range(65):
            out = out + "-"
        print(out)

def simulateFirstFit():
    mem = Memory()
    for i in range(15):
        mem.firstFitAllocate(MemoryContent("OBJ" + str(i), randint(1,8)))
    mem.printMemory()

def simulateBestFit():
    mem = Memory()
    for i in range(15):
        mem.bestFitAllocate(MemoryContent("OBJ" + str(i), randint(1, 8)))
    mem.printMemory()

def compareFirstAndBest():
    memFirst = Memory()
    memBest = Memory()
    contents = []
    for i in range(15):
        contents.append(MemoryContent("OBJ" + str(i), randint(1,8)))

    for j in range(len(contents)):
        memFirst.firstFitAllocate(contents[j])
    print("First Fit Memory Allocation")
    memFirst.printMemory()
    print()
    print()

    for k in range(len(contents)):
        memBest.bestFitAllocate(contents[k])
    print("Best Fit Memory Allocation")
    memBest.printMemory()
    print()
    print()



compareFirstAndBest()