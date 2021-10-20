import os
import shutil
import glob

original = r'C:/Users/selim/Desktop/A/arguments.txt'
target = r'C:/Users/selim/Desktop/B/arguments.txt'
shutil.copyfile(original, target)


path = "C:/Users/selim/Desktop/B"
listIN=os.listdir(path)
print(listIN)

path = "C:/Users/selim/Desktop/A/"

FileList=filter(os.path.isfile,glob.glob(path+"*"))

MaxFile=max(FileList, key=lambda x: os.stat(x).st_size)

print("Max File: ", MaxFile)
print('Max File size in bytes: ', os.stat(MaxFile).st_size)