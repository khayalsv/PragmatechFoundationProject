''' class car:
    suret=0
    reng=""
    def suretlen(self):
        self.suret+=1
x=car()
x.suret=90
x.suretlen()
print("suret",x.suret)

y=car()
y.suret=60
y.suretlen()
print("y sureti", y.suret)

z=car()
z.reng="qirmizi"
print(z.reng) '''


''' cars=[]

class car:
    def __init__(self,model,reng,suret,qapi):
        self.model=model
        self.reng=reng
        self.suret=suret
        self.qapi=qapi
    def addTooList(self):
        cars.append(self)
    def showCar(self):
        print(f'{self.model},{self.reng},{self.suret},{self.qapi},')
        

def createCar():
    model=input("model: ")
    reng=input("reng: ")
    suret=input("suret: ")
    qapi=input("qapi: ")

    x=car(model,reng,suret,qapi)
    x.addTooList()

while True:
    emr=input('Tamam mi davam mi (T/D): ')

    if emr=='T':
        for x in cars:
            x.showCar()
        break
    else:
        createCar() '''
    

''' gallery=[]

class car:
    def __init__(self,marka,model,reng,qiymet):
        self.marka=marka
        self.model=model
        self.reng=reng
        self.qiymet=qiymet
    
    def addToList(self):
        gallery.append(self)
    def showCar(self):
        print(f"{self.marka},{self.model},{self.reng},{self.qiymet},")

def createCar():
    marka=input("marka: ")
    model=input("model: ")
    reng=input("reng: ")
    qiymet=input("qiymet: ")
    x=car(marka,model,reng,qiymet)

    x.addToList()
    

while True:
    emr=input("Yeni masin elave edilsinmi ? (Y/N): ")

    if emr=="Y":
        createCar()
    elif emr=="N":
        for x in gallery:
            x.showCar()
        break '''


""" kitablar=[]

class kitab:
    
    def __init__(self,id,ad,yazar,sehife):
        self.id=id
        self.ad=ad
        self.yazar=yazar
        self.sehife=sehife
    
    def addToList(self):
        kitablar.append(self)
    def showKitab(self):
        print(f"{self.id},{self.ad},{self.yazar},{self.sehife},")
    def artsn(self):
        self.id+=1

id=0

def createKitab():
    global id
    ad=input("ad: ")
    yazar=input("yazar: ")
    sehife=input("sehife: ")

    yenikitab=kitab(id,ad,yazar,sehife)

    yenikitab.addToList()    

    yenikitab.id=id
    yenikitab.artsn()
    id+=1
    

def removeKitab():
    yenikitab.id=id
    kitablar.remove()
    

    


while True:
    emr=input("Enter: ")

    if emr=="1":
        createKitab()
    
    if emr=="2":
        for yenikitab in kitablar:
            yenikitab.showKitab()
        

    if emr=="3":
        removeKitab()   
 """


    


        



    
