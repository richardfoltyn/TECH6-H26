# Installing & configuring git on Windows

## Installing git

1. Download the installer [here](https://git-scm.com/download/win).
2. The installer allows you to tweak various things; just accept the defaults.
3. One setting you should change is the editor used for commit messages.
  A sensible choice is [nano](https://www.howtogeek.com/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/)
  (a simple command-line editor).
4. Once installed, git can be used via the command line by
    launching `Git Bash` from the start menu.


## Configuration

Before using git, you need to set your name and email address.
Open the `Git Bash` terminal
and type the following (you can use another email address, but if
you plan to use GitHub, use the same email address for both):

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@student.nhh.no
```
