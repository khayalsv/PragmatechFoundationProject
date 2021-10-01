import json
from os import umask

file=open("city.json","r")

data=file.read()

getDataFromJson=json.loads(data)

world=[]


def findLongName(name):
    LongName=""
    for e in name:
        if len(e)>len(LongName):
            LongName=e
    print(LongName)

def findLongNameCity(name):
    LongName=""
    for e in name:
        if len(e)>len(LongName):
            LongName=e
    print(f'{LongName} country {x["country"]}')


while True:
    command=input("Enter: ")

    if command=="1":
        country=input("country: ")
        for x in getDataFromJson:
            if x['country']==country:
                print(f'{x["country"]} city {x["city"]}')
        break
                

    if command=="2":
        country=input("country: ")
        for x in getDataFromJson:
          if x['country']==country:
            y=x["population"]
            world.append(y)
        a=max(world)
        b=min(world)
        print(a-b)
        break


    if command=="3":
        for x in getDataFromJson:
            c=(f'{x["country"]} coordinate {x["lat"]} {x["lng"]}')
            world.append(c)
        findLongName(world)
        break
    
    
    if command=="4":
        for x in getDataFromJson:
            c=(f'{x["city"]}')
            world.append(c)
        findLongNameCity(world)
        break
    

    elif command=="0":
        break




