import os


# getting all files in download folder.

def get_files():
    download_folder_files = []
    for file in os.listdir("C:/Users/opeyemi/Downloads"):
        download_folder_files.append(file)
    return download_folder_files


# getting all txt files in download folder.

def get_txt_files(download_folder_files):
    for file in download_folder_files:
        if file[-4:] == ".txt":
            print(file)


get_txt_files(get_files())
