import json
file=open("sample.json","r")

x=file.read()
Xunderstand=json.loads(x)  #jsondaki x-i python basa duseceyi sekilde cevirir

print(Xunderstand)