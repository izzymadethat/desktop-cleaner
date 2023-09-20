""" Clean The Desktop And Organize Files."""
import os
import datetime

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
    message = f"You have moved {counted_files} files from your Desktop."
    return message


def show_files_organized(files):
    """ Return exact files moved."""
    extension_counts = {}
    for extension in files:
        _, file_extension = os.path.splitext(extension)
        ext_name = file_extension.lower() # removes the dot in extensions list

        if ext_name in extension_counts:
            extension_counts[ext_name] += 1
        else:
            extension_counts[ext_name] = 1

    return extension_counts


test = check_if_file()
ext_test = get_file_extension(test)


files_organized = count_files_organized(test)
files_moved = show_files_organized(test)


# Save file to .txt log
with open('log_file.txt', 'w', encoding='utf-8') as file:
    # Write Headline
    file.write("\t\t=== Desktop Clean ===\n")
    file.write("\t\t\t Entry Log\n\n")
    today = datetime.datetime.now()

    # Write Cleanup information
    file.write(f"{files_organized}\n\n")
    file.write("Count\t\t\tFile\n")
    for extension, count in files_moved.items():
        file.write(f"{count} ........... \t{extension[1:]}\n")

    # Display file names just in case.
    file.write("\n\nFiles that were moved...\n")
    for file_name in test:
        file.write(f"{file_name}\n")

    file.write("\n\n\t\t Log Details:\n")
    file.write(f"Log saved {today}")
