# Installing & configuring git on macOS (Apple)

## Checking whether git is already installed

Git may already be installed on your machine. To check this, open the
[Terminal](https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac)
and type
```bash
git --version
```
If this returns without an error message, you already have git installed
and can skip the next step.


## Installing git

### Alternative 1

Git is shipped as part of the Apple Developer Command Line Tools. You
can install these by typing the following in the terminal:
```bash
xcode-select --install
```
and follow the instructions. See [this guide](https://mac.install.guide/commandlinetools/4) for details.

### Alternative 2

You can alternatively install git from [homebrew](https://brew.sh/).
Homebrew is not part of macOS and needs to be installed first, see
[this video guide](https://youtu.be/B4qsvQ5IqWk).

In short, you need to execute the following command in the terminal
to first install homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Once this is complete, you can install git with the following command:
```bash
brew install git
```
To verify that git was installed, paste the following into the terminal:
```bash
git --version
```
If you encounter problems along the way, watch the video linked above
for more detailed instructions.


## Configuration

Before using git, you need to set your name and email address. Open the terminal
and type the following (you can use another email address, but if
you plan to use GitHub, use the same email address for both):

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@student.nhh.no
```

***
# GitHub integration

## SSH keys for GitHub (optional)

If you plan to interact with GitHub only via Visual Studio Code, you can skip setting up
an SSH key.

In order to seamlessly access your remote repositories on GitHub in the terminal,
you *may* need to create an SSH key on your local computer and
add it to your GitHub account.

To create the SSH key, **copy** the following commands into the terminal:

```bash
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519_gh
cat ~/.ssh/id_ed25519_gh.pub
```
If everything worked, the last line of the output is your public
key which needs to be added to your GitHub account. It should look
something like this:
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKjhZ7rUTC3ldXmp+dBOShXU8907YVHVWV3T7ciJ3xoW
```
See [these instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account)
on how to add the key to your GitHub account.
