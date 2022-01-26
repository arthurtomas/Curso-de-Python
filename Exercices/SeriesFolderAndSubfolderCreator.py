import shutil
import getpass
import os

# Inputs
m_folder = input("Series name: ")
num_sub_folders = int(input("Number of Seasons: "))
user = getpass.getuser()


def delete_folder(directory):
    shutil.rmtree(directory)


def dir_exists(directory):
    return os.path.exists(directory)


def create_folder(directory):              # Function responsible to create folders
    os.mkdir(directory)


if dir_exists(f"C:\\Users\\{user}\\Desktop\\{m_folder}"):
    answer = input("This folder already exists. Would you like to delete it and create a new one? (Y/N): ")
    if answer in "Nn":
        print("Ok, we kept your original folder and its content.")
    elif answer in "Yy":
        delete_folder(f"C:\\Users\\{user}\\Desktop\\{m_folder}")
        create_folder(f"C:\\Users\\{user}\\Desktop\\{m_folder}")
        for i in range(1, num_sub_folders + 1):
            create_folder(f"C:\\Users\\{user}\\Desktop\\{m_folder}\\{i}° Season")
    else:
        print("You didn't enter a valid answer!")
elif not dir_exists(f"C:\\Users\\{user}\\Desktop\\{m_folder}"):
    create_folder(f"C:\\Users\\{user}\\Desktop\\{m_folder}")
    for i in range(1, num_sub_folders + 1):
        create_folder(f"C:\\Users\\{user}\\Desktop\\{m_folder}\\{i}° Season")

