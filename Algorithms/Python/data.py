import json

ad=input("ad: ")
soyad=input("soyad: ")

dct={
    "ad":ad,
    "soyad":soyad
}

file=open("sample.json","r")  #sample.json fayli ile elaqe qururug r ile oxuma meqsedin seciriy

x=file.read()  #bu metod fayil icindeki melumati goturub, sora x deyisenine yukledim

Xunderstand=json.loads(x)  #jsondaki x-i python basa duseceyi sekilde cevirir

Xunderstand.append(dct) #artiq list olduguna gore dct elave edirik

convertXToJson=json.dumps(Xunderstand)  #listi jsonun basa duseceyi formata saliriq

file=open('sample.json','w')  #her yazanda ("w" herfi ile) qabi tezeliyib elave edirik.

file.write(convertXToJson) #fayli yazdiririq

