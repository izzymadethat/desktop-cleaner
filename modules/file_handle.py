import os
import shutil
import datetime
from modules.folder_manager import create_folder


class File():

    def __init__(self):
        self.extensions = {}
        self.files = []
        self.audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")
        self.video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")
        self.img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")
        self.document = (".txt", ".pdf", ".csv", ".doc", ".xls")
        self.zip = (".zip", ".b1", ".rar")
        self.setup = (".exe",".iso")
    
    def check_if_files(self, directory):
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                if not file_path.endswith('.lnk'):
                    self.files.append(file)

    def count(self, files):
        """Returns the number of files moved."""

        counted_files = len(self.files)
        message = f"You have moved {counted_files} files from your Desktop."
        return message

    def get_extensions(self):
        """ Return exact files moved."""
        # extension_counts = {}
        for extension in self.files:
            _, file_extension = os.path.splitext(extension)
            ext_name = file_extension.lower() # removes the dot in extensions list

            if ext_name in self.extensions:
                self.extensions[ext_name] += 1
            else:
                self.extensions[ext_name] = 1
    
    def move(self, path, folders):
        today = self.get_current_day()

        create_folder(path, folders, today)
               
        for file in self.files:
            if self.is_audio(file):
                self.move_to_folder(path, file, 'Audio Files', today)
            elif self.is_video(file) or self.is_image(file):
                self.move_to_folder(path, file, 'Media Files', today)
            elif self.is_document(file):
                self.move_to_folder(path, file, 'Document Files', today)
            elif self.is_compressed(file):
                self.move_to_folder(path, file, 'Zip Files', today)
            elif self.is_setup(file):
                self.move_to_folder(path, file, 'Setup Files', today)
            else:
                self.move_to_folder(path, file, 'Files To Be Reviewed', today)


    # Extension Checks
    def is_audio(self, file):
        return os.path.splitext(file)[1] in self.audio
    def is_video(self, file):
        return os.path.splitext(file)[1] in self.video
    def is_image(self, file):
        return os.path.splitext(file)[1] in self.img
    def is_document(self, file):
        return os.path.splitext(file)[1] in self.document
    def is_compressed(self, file):
        return os.path.splitext(file)[1] in self.zip
    def is_setup(self, file):
        return os.path.splitext(file)[1] in self.setup

    def move_to_folder(self, path, file, new_folder, current_day):
        shutil.move(os.path.join(path, file), os.path.join(path, new_folder, current_day))
        print(f"{file} moved successfully to {new_folder}.")

    def get_current_day(self):
        now = datetime.datetime.now()
        date = now.strftime("%m_%d")
        
        return date