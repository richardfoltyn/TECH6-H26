# Frequently used git commands

These commands work in the macOS (Apple) 
[Terminal](https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac) 
application, the 
[Git Bash](https://www.gitkraken.com/blog/what-is-git-bash) 
on Windows, as well as the bash shell on Linux.

-   Note that in the examples below, the `#` is the start of a comment and not
    part of the actual command.
-   In general, avoid spaces in file and folder names. If you must use spaces,
    you need to wrap the name in double quotes like this `"file name.py"`.
-   Most of these commands must be run from *within* a git repository.

## `git init`: initialize new git repository

By default, the git repository is created in the current folder.

### Examples
```bash
git init                # Initialize git repository, use default name 
                        #   for main branch
git init -b main        # Initialize git repository, use "main" as name 
                        #   for main branch
```

## `git add`: add files to git

### Examples

```bash
git add example.py      # Add file "example.py" from the current folder
git add .               # Add all files in current folder and 
                        #   its subfolders
```
      
## `git rm`: remove file from git

*Warning:* files removed with `git rm` are also removed from your computer!

### Examples

```bash
git rm example.py       # Remove "example.py" from git and delete the file
```

## `git mv`: move (or rename) files

### Examples
```bash
git mv example1.py example2.py  # Rename file "example1.py" to "example2.py"
```


## `git commit`: commit changes

New and updated files must first be added using `git add`.

### Examples

```bash
git commit                      # Commit changes 
                                #   (opens editor for commit message)
git commit -m "Commit message"  # Commit changes, specify commit 
                                #   message directly
```


## `git status`: show status of the working tree

Shows files that have been modified, added, or deleted from the working tree.

## `git diff`: show differences

Shows line-by-line differences for each new or updated file.

## `git log`: show commit history

Shows a list of prior commits.

## `git push`: push changes to remote repository (e.g., GitHub)

Note that a remote repository needs to be defined before running this command.
It is set automatically if the repository was cloned from the remote.

### Examples

```bash
git push
git push -u origin main     # Push branch "main" to remote "origin"
```

## `git pull`: pull changes from remote repository (e.g., GitHub)

### Examples

```bash
git pull                    # Pull new commits from remote
```

## `git clone`: clone a remote repository to your computer 

By default, the remote repository will be cloned inside the current directory.

### Examples
```bash
git clone https://github.com/richardfoltyn/TECH6-H26.git
```


## `git remote`: manage remote repositories

`git remote` and its subcommands can be used to add or modify the URL 
used for your remote repository.

### Examples

To add a remote using HTTPS, use something like this:
```bash
git remote add origin https://github.com/richardfoltyn/TECH6-H26.git
git push -u origin main             # Push the main branch to the remote
```

To add a remote using SSH keys for authentication, use something like this:
```bash
git remote add origin git@github.com:richardfoltyn/TECH6-H26.git
git push -u origin main             # Push the main branch to the remote
```