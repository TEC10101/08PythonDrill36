import shutil
import os
import pdb


pdb.set_trace()

#shutil.move(src, dst, copy_function=copy2)
source = 'C:\\Projects\\Python\\pythonDrills\\moveFolder\\Folder_A\\'
destination = 'C:\\Projects\\Python\\pythonDrills\\moveFolder\\Folder_B\\'

files = os.listdir(source)

for f in files:
	print(f)
# shutil.move(source, destination)
