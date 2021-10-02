import json


file=open("city.json","r")

data=file.read()

getDataFromJson=json.loads(data)

world=[]

lst=[]


def findLongName(name):
    LongName=""
    for e in name:
        if len(e)>len(LongName):
            LongName=e
    print(f'{LongName} coordinate {x["lat"]} {x["lng"]}')


def findLongNameCity(name):
    LongName=""
    for e in name:
        if len(e)>len(LongName):
            LongName=e
    print(f'{LongName} country {x["country"]}')


def closest(lst, K):
      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]


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
            y=(f'{x["country"]}')
            world.append(y)
        findLongName(world)
        break
    
    
    if command=="4":
        for x in getDataFromJson:
            y=(f'{x["city"]}')
            world.append(y)
        findLongNameCity(world)
        break
    

 

    if command=="5":
        for x in getDataFromJson:
            y=(f'{x["lat"]}')
            a=(f'{x["country"]}')
            lst.append(float(y))
            K=0
        print(closest(lst , K)) 
        

             
        

            

    elif command=="0":
        break




