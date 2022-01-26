import os

source = "folder"
destination = "C:\\Users\\Barzilay\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(f"{source} was moved")
except FileNotFoundError:
    print(f"{source} was not found")
