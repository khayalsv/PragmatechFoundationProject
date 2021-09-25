bus=[]

class passanger:
    def __init__(self,which,name,age,whence,size):
        self.which=which
        self.name=name
        self.age=age
        self.whence=whence
        self.size=size

    def addToBus(self):
        bus.append(self)
    
    def showInformation(self):
        print(f"which: {self.which}, name: {self.name}, age: {self.age}, whence: {self.whence}, size: {self.size}")

which=0
def GetIn():
    global which
    which+=1
    name=input("name: ")
    age=input("age:")
    whence=input("whence: ")
    size=input("size: ")

    newpassanger=passanger(which,name,age,whence,size)
    newpassanger.addToBus()

def GetOff(which):
    for newpassanger in bus:
        if int(which)==newpassanger.which:
           bus.remove(newpassanger)
           break

while True:
    command=input("enter: ")
    
    if command=="1":
        GetIn()

    if command=="2":
        for newpassanger in bus:
            newpassanger.showInformation()

    if command=="3":
        which=input("dusen: ")
        GetOff(which)