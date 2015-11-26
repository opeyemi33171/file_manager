import os


# getting all files in download folder.

def get_files():
    download_folder_files = []
    for file in os.listdir("C:/Users/opeyemi/Downloads"):
        download_folder_files.append(file)
    return download_folder_files


# getting all txt files in download folder.

def get_txt_files(download_folder_files):
    txt_files = []
    for file in download_folder_files:
        if file[-4:] == ".txt":
            txt_files.append(file)
    return txt_files


# print (get_txt_files(get_files()))

def move_txt_files(txt_files):
    for file in txt_files:
        os.rename("C:/Users/opeyemi/Downloads/%s" % file, "C:/Users/opeyemi/Documents/%s" % file)

move_txt_files(get_txt_files(get_files()))
