import os
import shutil
#command for cheking your path 
# print(os.getcwd())

# for creating a new file
# print(os.mkdir('movies'))

#rocheck whether a file exist or not
# print(os.path.exists('movies'))

# if os.path.exists('movies'):
#     print("already exsits")
# else:
#     os.mkdir('movies')

#make a new file
# open('file.txt','a').close() 

#to print the list of items in the folder
# print(os.listdir())


# for item in os.listdir():
    # print(r'C:\Users\RAHUL\OneDrive\Documents\python\Week4'+'\\'+ item)
    # path=os.path.join(os.getcwd(),item)
    # print(path)

# for creating list of all files and folders at a path
# filefilter=os.walk(r'C:\Users\RAHUL\OneDrive\Documents\python')
# for current_path,folder_names,file_names in filefilter:
#     print(f"currentpath: {current_path}")
#     print(f"folder_names: {folder_names}")
#     print(f"file_names: {file_names}")

#for deleting file or folder
# os.rmdir('movies')

# creting folder inside a folder
# os.makedirs('new/movies/music')

# for deleting permanentaly
# shutil.rmtree('new')

# copy 
# shutil.copytree('new','documents/new221321')





