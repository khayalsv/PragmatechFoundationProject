import json

ad=input("ad: ")
soyad=input("soyad: ")

dct={
    "ad":ad,
    "soyad":soyad
}


convertToJson=json.dumps(dct)   #jsonun basa duseceyi formata cevilir

file=open("sample.json","w")

file.write(convertToJson)

