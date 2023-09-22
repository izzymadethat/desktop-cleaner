"""This File Handles all file moving functions."""

import os
import shutil


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

document = (".txt", ".pdf", ".csv", ".doc", ".")

zip_file = (".zip", ".b1", ".rar", ".iso")

setup_file = (".exe")


def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_document(file):
    return os.path.splitext(file)[1] in document

def is_zip(file):
    return os.path.splitext(file)[1] in zip_file

def is_setup(file):
    return os.path.splitext(file)[1] in setup_file



def move_all_files(folder_path, current_day):
    os.chdir("/Users/Isaiah Vickers/Desktop")
    for file in os.listdir():
        if is_audio(file):
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'Audio Files', current_day))
        elif is_image(file) or is_video(file):
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'Media Files', current_day))
        elif is_document(file):
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'Documents', current_day))
        elif is_zip(file):
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'Zip Files', current_day))
        elif is_setup(file):
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'Setup Files', current_day))
        else:
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, 'Files To Be Reviewed', current_day))
