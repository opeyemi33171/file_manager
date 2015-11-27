import os, time


# getting all files in download folder.

def get_files():
    download_folder_files = []
    for file in os.listdir("C:/Users/opeyemi/Downloads"):
        download_folder_files.append(file)
    return download_folder_files


# getting all txt files in download folder.

def move_to_destination(download_folder_files):
    for file in download_folder_files:
        if file[-4:] == ".txt" or file[-4:] == ".pdf" or file[-4:] == ".iso" or file[-5:] == ".docx" or file[
                                                                                                        -4:] == ".zip":
            os.rename("C:/Users/opeyemi/Downloads/%s" % file, "C:/Users/opeyemi/Documents/%s" % file)
        elif file[-4:] == ".mp3" or file[-4:] == ".wma":
            os.rename("C:/Users/opeyemi/Downloads/%s" % file, "C:/Users/opeyemi/Music/%s" % file)
        elif file[-4:] == ".exe":
            os.rename("C:/Users/opeyemi/Downloads/%s" % file, "C:/Users/opeyemi/Desktop/Executables/%s" % file)
        elif file[-4:] == ".jpg" or file[-4:] == ".png":
            os.rename("C:/Users/opeyemi/Downloads/%s" % file, "C:/Users/opeyemi/Pictures/%s" % file)


while True:
    move_to_destination(get_files())
    time.sleep(60)

"""
# print (get_txt_files(get_files()))

def move_txt_files(txt_files):
    for file in txt_files:
        os.rename("C:/Users/opeyemi/Downloads/%s" % file, "C:/Users/opeyemi/Documents/%s" % file)

move_txt_files(get_txt_files(get_files()))
"""
