import os

def rename_files():
    file_list = os.listdir(r"C:\")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))


rename_files()
