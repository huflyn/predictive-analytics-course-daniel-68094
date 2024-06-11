import os
from os import walk
import tempfile

# current working directory
cwd = os.getcwd()
print("current working directory: ", cwd)

# location temp folder
tmp = tempfile.gettempdir()
print("temp folder: ", tmp)

filetypes = [".py"]

# list files/folders
for (dirpath, dirnames, filenames) in walk("."):
    for file in filenames:
        if file.lower().endswith(".py".lower()):
            print(dirpath + "/" + file)
            inFile = open(dirpath + "/" + file, "r")
            content = inFile.read()
            inFile.close()
            global outFile
            outFile = open(tmp + "/outfile.py", "a")
            outFile.write(content)

outFile.close()