# Frequently used shell commands

These commands work in the macOS (Apple) 
[Terminal](https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac) 
application, the 
[Git Bash](https://www.gitkraken.com/blog/what-is-git-bash) 
on Windows, as well as the bash shell on Linux.

-   Note that in the examples below, the `#` is the start of a comment and not
    part of the actual command.
-   In general, avoid spaces in file and folder names. If you must use spaces,
    you need to wrap the name in double quotes like this `"file name.py"`.

## `cd`: change directory

### Examples
```bash
cd                      # Change to home directory
cd python               # Change to folder "python"
cd "Python 3.12"        # Change to folder "Python 3.12". 
                        # Quotes are required if the name contains spaces.
cd ..                   # Change to the parent directory
```

## `ls`: list files and directories

### Examples
```bash
ls                      # List contents of current folder
ls python               # List contents of folder "python"
ls -l example.py        # Show detailed info about file "example.py"
```
## `pwd`: print working directory

### Examples
```bash
pwd                     # Print the path of the current working directory
```

## `mkdir`: make directory

### Examples
```bash
mkdir python            # Create folder "python" in the current folder
mkdir "Python 3.12"     # Create folder "Python 3.12" in the current folder.
                        #   Quotes are required if the name contains spaces.
```

## `rm`: remove file or folder

### Examples

```bash
rm example.py           # Delete file "example.py" in the current folder.
rm -rf python           # Delete the folder "python" and ALL the files and 
                        #   subfolders contained in it.
                        #   WARNING: this cannot be undone.
```

## `cat`: print the contents of a file in the terminal

### Examples

```bash
cat example1.py         # Print the contents of "example1.py"
```