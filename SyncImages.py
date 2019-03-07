import os
import shutil

source = input('Enter source folder\n')
destination = input('Enter destination folder\n')

os.chdir(source)
list1 = [file for file in os.listdir() if file.split('.')[1] in ('png','jpg','jpeg')]

##print(list1,len(list1))

os.chdir(destination)


list2 = [each for each in os.listdir() if each.split('.')[1] in ('png','jpg','jpeg')]

list3 = [each for each in list1 if each not in list2]

##print(list3,len(list3))            

os.chdir(source)
if len(list3)!=0:        
    for each in list3:
        shutil.copy2(each,destination)
    print('{} Images synced successfully.'.format(len(list3)))

else :
    print('All images already synced.')
