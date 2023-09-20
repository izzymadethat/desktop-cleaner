""" Clean The Desktop And Organize Files."""
import os

def check_if_file():
    """Check through the directory to make sure I am returning files."""
    directory = r'C:\\Users\\Isaiah Vickers\Desktop'
    files = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            files.append(file)
    return files

def get_file_extension(files_list):
    """Return a list of extensions for later use.
    This code splits each file found in check_if_file then add the ext
    to a list set so that I can make sure each file ext is stored properly."""

    extensions = set()
    for file in files_list:
        file_extension = os.path.splitext(file)[1]
        extensions.add(file_extension)
    return list(extensions) # returns one of each ext in list (Ex.".mp3")

def count_files_organized(files):
    """Returns the number of files moved."""

    counted_files = len(files)
    message = f"You have moved {counted_files} files."
    print(message)

    # Get exact files moved.
    extension_counts = {}
    for extension in files:
        _, file_extension = os.path.splitext(extension)
        ext_name = file_extension.lower() # removes the dot in extensions list

        if ext_name in extension_counts:
            extension_counts[ext_name] += 1
        else:
            extension_counts[ext_name] = 1

    # Print the count of each extension
    for extension, count in extension_counts.items():
        if count == 1:
            print(f"{count} {extension[1:]} file moved.")
        else:
            print(f"{count} {extension[1:]} files moved.")


test = check_if_file()
ext_test = get_file_extension(test)
count_files_organized(test)

# print(count_test)
