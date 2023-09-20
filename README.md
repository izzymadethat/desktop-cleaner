# desktop-cleaner

This app is designed simply to clean a cluttered desktop. It does so by moving
files into folders based on their extensions. When it is done (within seconds),
it will print a confirmation log to display the details of each transfer.

## features:

### check_if_file()

Runs through entire desktop directory and ONLY finds actual files with extensions.

Directories and File Folders excluded.

### get_file_extension()

Provides all extensions removed (returns one of each extension) so that
log can be provided and future folders created for extensions not in list.

### count_files_organized()

Returns exact number of files moved.

### show_files_organized()

Returns dictionary of file extensions moved.
