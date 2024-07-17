#inharitance vs composition
class CPU:
    def __init__(self,cores) -> None:
        self.core = cores

class RAM:
    def __init__(self,size) -> None:
        self.size = size

class HardDrive:
    def __init__(self,capacity) -> None:
        self.capacity = capacity

#computer has a cpu
#computer has a ram
#computer has a hardDisk
class Computer:
    def __init__(self,core,ram_sz ,hd_capacity ) -> None:
        self.core = CPU(core)
        self.ram_size = RAM(ram_sz)
        self.hardDisk_capacity = HardDrive(hd_capacity)


mac = Computer(8,16,512)

