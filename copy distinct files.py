import os
import shutil


source = "C:/Users/Admin/Downloads/" ##input("Please enter source folder")

os.chdir('C:/Users/Admin/Desktop/')
os.mkdir('temp_destination')
temp = "C:/Users/Admin/Desktop/temp_destination/"

## set destination of your choice
destination = "C:/Users/Admin/Desktop/TestPython/"
os.mkdir(destination)
##empty temp destination
os.chdir(temp)

for each in os.listdir():
    os.remove(each)

print("1")
##change directory of files to spotlight wallpaper folder
os.chdir(source)

l1 = [file for file in os.listdir() if len(file.split('.'))>1 and file.split('.')[1] in ('jpg','png','jpeg')]

##copy file to destination folder
for file in l1:
    shutil.copy2(file,temp)

print("2")
## change extension to jpg
os.chdir(destination)


l2 = [each for each in os.listdir()]
    
print("l1 : {}".format(l1))

print("\nl2 : {}".format(l2))
for each in l1:
    for file in l2:
        if each==file:
            pass
        else:
            shutil.copy2(each,destination)

print("\nl2 : {}".format(l2))
os.chdir(temp)
for each in os.listdir():
    os.remove(each)

os.chdir('..')
os.rmdir(temp)
print("all done")    

