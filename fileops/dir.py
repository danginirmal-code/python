##Create a new directory
import os
# new_directory="package"
# os.mkdir(new_directory)
# print(f"Directory {new_directory} created" )

items=os.listdir('.')
print(items)


##joining paths
dir_name="folder"
file_name="file.txt"
full_path=os.path.join(dir_name,file_name)
print(full_path)

dir_name="folder"
file_name="file.txt"
full_path=os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)

#check path exist or not
path="example1.txt"
if os.path.exists(path):
    print(f"The path {path} exist")
else:
    print(f"The path {path} doesnot exist")

realtive_path="example.txt"
absolute_path=os.path.abspath(realtive_path)
print(absolute_path)