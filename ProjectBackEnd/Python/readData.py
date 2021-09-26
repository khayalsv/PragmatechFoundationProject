import json

file=open("sample.json","r")

data=file.read()

converjson=json.loads(data)

ad=input("ad tap: ")

for user in converjson:
    if user['ad']==ad:   #--bu setir olmasa adlari tapir
        print(f'{user["ad"]} istifadecin soyadi {user["soyad"]}')

