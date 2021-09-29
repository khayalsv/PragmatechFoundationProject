import json

ad=input("ad: ")
soyad=input("soyad: ")

dct={
    "ad":ad,
    "soyad":soyad
}

file=open("sample.json","r")  #sample.json fayli ile elaqe qururug r ile oxuma meqsedin seciriy

x=file.read()  #bu metod fayil icindeki melumati goturub, sora x deyisenine yukledim

getXfromJson=json.loads(x)  #jsondaki x-i python basa duseceyi sekilde liste cevirir

getXfromJson.append(dct) #artiq list olduguna gore dct elave edirik

convertXToJson=json.dumps(getXfromJson)  #listi jsonun basa duseceyi formata saliriq

file=open('sample.json','w')  #her yazanda ("w" herfi ile) qabi tezeliyib elave edirik.

file.write(convertXToJson) #fayli yazdiririq


""" ad=input("ad tap: ")

for user in getXfromJson:
    if user['ad']==ad:   #--bu setir olmasa adlari tapir
        print(f'{user["ad"]} istifadecin soyadi {user["soyad"]}') """
