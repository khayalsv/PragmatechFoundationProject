""" istifadeci=[]


while True:
    emr=input('yeni istifadeci elave edilsinmi (1/2):')
    
    if emr=='1':
        ad=input("ad: ")
        soyad=input("soyad: ")
        yas=input("yas: ")
        email=input("email: ")
        istifadeci.extend([ad,soyad,yas,email])

    

    elif emr=='2':
        print(istifadeci)
        break """




library=[]

import json
f=open("sample.json","w")


class book:
    def __init__(self,id,name,author,page):
        self.id=id
        self.name=name
        self.author=author
        self.page=page

    def addToLibrary (self):
        library.append(self)
    
    def showList(self):
        print(f"ID:{self.id}, Name:{self.name}, Author:{self.author}, Page:{self.page}")


id=0
    
def createBOOK():
    global id
    id+=1

    name=input("name: ")
    author=input("author: ")
    page=input("page: ")

    newbook=book(id,name,author,page)
    f.write(f"ID:{id}, Name:{name}, Author:{author}, Page:{page}\n")
    newbook.addToLibrary()
    



def removeBOOK(id):
    for newbook in library:
        if int(id)==newbook.id:
            library.remove(newbook)
            break

def editBOOK(id):
    for newbook in library:
        if int(id)==newbook.id:
            newbook.id=input("id: ")
            newbook.name=input("name: ")
            newbook.author=input("author: ")
            newbook.page=input("page: ")


def findID(id):
    for newbook in library:
        if int(id)==newbook.id:
            newbook.showList()
            break

def findNAME(name):
    for newbook in library:
        if name==newbook.name:
            newbook.showList()
            break


 

while True:
    command=input("Enter: ")
    
    if command=="1":
        createBOOK()
    

    if command=="2":
        for newbook in library:
            newbook.showList()
    
    if command=="3":
        id=input("delete book:")
        removeBOOK(id)
    
    if command=="4":
        id=input("edit book: ")
        editBOOK(id)

    if command=="5":
        id=input("find id book: ")
        findID(id)
    
    if command=="6":
        name=input("name: ")
        findNAME(name)

    elif command=="7":
        break
