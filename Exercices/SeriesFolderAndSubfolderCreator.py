import os

# Inputs
m_folder = input("Series name: ")
num_sub_folders = int(input("Number of Seasons: "))


def create_folder(directory):              # Function responsible to create folders
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
    except OSError:
        print("Error")


# Create the main folder
create_folder(f"C:\\Users\\Barzilay\\Desktop\\{m_folder}")

# Loop for creating the seasons folders
for i in range(1, num_sub_folders+1):
    create_folder(f"C:\\Users\\Barzilay\\Desktop\\{m_folder}\\{i}° Season")

