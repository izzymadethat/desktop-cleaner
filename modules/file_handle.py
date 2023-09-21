import os

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
