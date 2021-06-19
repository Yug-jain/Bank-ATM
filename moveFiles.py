import os
import shutil

source=input("Enter Source Folder Name")
destination=input("Enter Destination Folder Name")

source=source+"/"
destination=destination+"/"

list_of_file=os.listdir(source)

for file in list_of_file:
    shutil.move((source+file),destination)
    