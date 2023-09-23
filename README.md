# Desktop Cleaner by _IzzyMadeThat_

This app is designed simply to clean a cluttered desktop. It does so by moving
files into folders based on their extensions. When it is done (within seconds),
it will print a confirmation log to display the details of each transfer.

## how to use:

- Simply run the application (no interface will show)
- The app will run through all files on your desktop that are not shortcut files or folders
- Each file will be moved to a created folder based on it's extension (any music files will be storder in 'Audio Files')
- Once done, head to your Documents/Dekstop Cleaner/ and find the date folder which has the log to show you what was moved.

# _For Open Source Contributors:_

If you would like to make any contributions, I would be more than happy! Just simply fork out the main branch and work on whatever you would like to see. Then send me a pull request and I'll check it out as soon as possible.

I'm also ALWAYS open to room for improvement! I have the following features below.

## features:

### check_if_file()

Runs through entire desktop directory and ONLY finds actual files with extensions.

File Directories and Shortcut Files excluded.

### get_file_extension()

Provides all extensions removed (returns one of each extension) so that
log can be provided and future folders created for extensions not in list.

### count_files_organized()

Returns exact number of files moved.

### show_files_organized()

Returns dictionary of file extensions moved.

## expected future releases:

- Shows exactly the folder where files were moved as it's running.
- GUI that shows alerts and allows users to store specific files in specific folders
- More in-depth system displays (shows you which files are being moved at the current moment.)
- Database for more accurate log reporting.
