# MEDomicsTools Linux Tips

This document presents some Linux tips and tricks to improve your Linux experience.

## Table of Contents
- [MEDomicsTools Linux Tips](#medomicstools-linux-tips)
  - [Table of Contents](#table-of-contents)
  - [Contributors](#contributors)
  - [Changelog](#changelog)
  - [To-Do](#to-do)
  - [## Standard](#-standard)
    - [R000 - Aliases](#r000---aliases)
    - [R001 - Terminal](#r001---terminal)
      - [**Overview**](#overview)
      - [**Terminal Window**](#terminal-window)
      - [**Terminal Tabs**](#terminal-tabs)
      - [**Terminal Display**](#terminal-display)
      - [**Terminal Input**](#terminal-input)
  - [**Using a Customized Terminal Prompt**](#using-a-customized-terminal-prompt)
    - [**Steps to install the prompt:**](#steps-to-install-the-prompt)
    - [R002 - Working Directory](#r002---working-directory)
    - [R003 - Absolute and Relative Path](#r003---absolute-and-relative-path)
    - [R004 - Basic Commands](#r004---basic-commands)
      - [**Directories**](#directories)
      - [**Files**](#files)
    - [R005 - Vim and Nano](#r005---vim-and-nano)
      - [Modes for Vim](#modes-for-vim)
      - [Exit and save](#exit-and-save)
      - [Search](#search)
    - [R006 - Saving terminal output to disk](#r006---saving-terminal-output-to-disk)
    - [R007 - SSH (Secure Shell)](#r007---ssh-secure-shell)
    - [**Using Custom Host Names For Your SSH Connections**](#using-custom-host-names-for-your-ssh-connections)
    - [R008 - SCP (Secure Copy)](#r008---scp-secure-copy)
    - [R009 - Using Git](#r009---using-git)
      - [**Getting Started**](#getting-started)
    - [R010 - Using Anaconda](#r010---using-anaconda)
      - [**Installing Anaconda**](#installing-anaconda)
      - [**Installing Miniconda**](#installing-miniconda)
      - [**Creating a Conda Environment**](#creating-a-conda-environment)
    - [R011 - Recommended Terminal Emulator](#r011---recommended-terminal-emulator)
      - [**Installing Kitty**](#installing-kitty)
      - [**Using Kittens**](#using-kittens)
      - [**Terminal Issues with SSH and kitty**](#terminal-issues-with-ssh-and-kitty)
    - [R012 - Using Tmux and Alternatives](#r012---using-tmux-and-alternatives)

NOTES: 

- To update the Table of Contents, use: https://ecotrust-canada.github.io/markdown-toc/
- Section headers cannot contain special characters other than -, otherwise the TOC hyperlinks will not work

## Contributors

- [Achille Lanctôt-Saumure](https://github.com/Troy-Boy)
- [Nicolas Raymond](https://github.com/Rayn2402)
- [Simon Giard-Leroux](https://github.com/sgiardl)

## Changelog

Revision | Date       | Description |
---------| -----------| ----------- |
A        | 2021-12-01 | Creation    |
A        | 2021-12-02 | Update      |
G        | 2022-02-15 | Update      |

## To-Do

- [x] Terminal pimping (check with Guillaume Cléroux) (Achille)
- [x] Paths/filesystem (Achille)
- [x] vim/nano (Achille)
- [x] Save terminal output to disk (Achille)
- [x] ssh (Achille)
- [x] scp (Nicolas)
- [ ] git (Started but not finished)
- [ ] Tmux
- [x] Kitty
- [ ] alias + bashrc (Nicolas: add stuff to Simon's part)

## Standard
---
### R000 - Aliases

Aliases are shorthands that can be created to shorten the length of common Linux terminal commands. In Ubuntu, you can add aliases at the end of the hidden '\~/.bashrc' OR '\~/.bash_aliases' files in the 'Home' directory. 

Although both are valid options, we recommend creating a separate '\~/.bash_aliases' file and adding this line to your '\~/.bashrc' file to make managing your aliases easier:

```
source ~/.bash_aliases
```

The following is a list of [Simon](https://github.com/sgiardl)'s Linux aliases:
```
# Custom aliases
alias gs="git status"
alias gd="git diff"
alias ga="git add"
alias ga.="git add ."
alias gc="git commit -m"
alias gpo="git push origin"
alias graph="git log --all --decorate --oneline --graph"
alias gpu="watch -d -n 0.5 nvidia-smi"
alias tb="tensorboard --logdir=logdir"
alias pk="pkill -f 'python'"
alias brc="source ~/.bashrc"
```
After modifying aliases, simply run the following command in your terminal to have access to them:
```
source ~/.bashrc
```
or, after the first time:
```
brc
```

It is possible to list the aliases with the command `alias` and remove one with `unalias <your custom alias>`.

---
### R001 - Terminal

If you are already familiar with the concept and use of the terminal in Linux, you can skip this section. If not, this will be a good rundown of the basics.

#### **Overview**

Shell, Prompt, Terminal or Console are all various names to describe the text interface. It is your best friend to understand and use proficiently Ubuntu. In the interface you can type in commands; they are a direct and flexible way to communicate with the operating system and can be easily copied from internet tutorials or docs. Following is a list of shortcuts related to the use of the terminal.

#### **Terminal Window**

- **Ctrl+Alt+T**: open terminal window.
- **Shift+Ctrl+Q**: close current terminal window.

#### **Terminal Tabs**

- **Shift+Ctrl+T**: open new tab.
- **Shift+Ctrl+W**: close current tab.
- **Shift+Ctrl+T**: open new tab.
- **Ctrl+PgUp**: switch previous tab.
- **Ctrl+PgDn**: switch next tab.

#### **Terminal Display**

- **Ctrl+S**: freeze the output, but let the program run in background.
- **Ctrl+Q**: restart the output, if it's been stop with **Ctrl+S**.
- **Shift+Ctrl+F**: search in the display.

#### **Terminal Input**

- **Shift+Ctrl+C**: copy highligthed text.
- **Shift+Ctrl+V**: paste from clipboard at the cursor position.

## **Using a Customized Terminal Prompt**

We recommend you install the [Starship Prompt](https://starship.rs/) to better use the terminal. It's a cross platform shell that has a lot of features, notably:
- Displaying the active Anaconda environment
- Showing which languages are used for the scripts in your current directory
- Letting you know which git branch you are currently working on, and if modifications are present
- And lots more...
  
### **Steps to install the prompt:**
1. You need to install a Nerd Font. We recommend the Hack Nerd Font Complete.
    ```
    sudo apt update && sudo apt install fonts-hack
    ```

2. Enabling the Hack Font in your terminal of choice. You can navigate to the preferences menu of your terminal and selecting the Hack Nerd Font Complete as your default font.
   
3. Downloading the starship prompt. (Commands for bash prompt only)
   ```
   sudo apt install curl && \
   sh -c "$(curl -fsSL https://starship.rs/install.sh)" && \
   echo '\n# Starting the starship prompt\neval "$(starship init bash)"' >> ~/.bashrc
   ```

4. Alternatively, if you are not a fan of emojis in your terminal prompt, you can replace them with symbols using this command
   ```
   sh -c "cd ~/.config && curl -O https://raw.githubusercontent.com/sgiardl/MEDomicsTools/main/Configs/starship.toml"
   ```


---
### R002 - Working Directory

An important concept of the terminal is the working directory. Ubuntu filesystem is like a tree, with the directory `/` as the **root directory**. Every other folder and file stem from the root. A subdirectory of the root is `home`, which has another subdirectory `<user>` ('\<user\>' is the current user on the session). 

The working directory is where you are in the filesystem **relatively** to the root directory. Say you open a terminal, your current working directory is `/home/<user>`. Hence here, relatively to the root `/`, you are in the subdirectory `home/<user>`.
The path `/home/<user>` is mapped to the abbreviation `~`; a path with `~/some/random/path` in Ubuntu will resolve to `/home/<user>/some/random/path`.

### R003 - Absolute and Relative Path

To understand the difference between relative and absolute path, consider the following statements:

1. The path from the root to any file or folder in the filesystem is an **absolute path**.
2. The path from your current working directory to any file or folder in the filesystem is the **relative path**.

**Any** path that starts with `/` or `~` is an **absolute path** and any path that does not is a **relative path**.

Say a filesystem contains the following structure:

    /
    |-- home/
    |   |-- <user>/
    |       |-- something/
    |           |-- some_file.txt
    |   ...
    ...

Opening a terminal window will set your current directory to `/home/<user>`. Now say you you need to access the text file. You could either use its absolute path, which would be either `/home/<user>/something/some_file.txt` or `~/something/some_file.txt` **or** its relative path, which would be `something/some_file.txt` **or** `./something/some_file.txt`.

### R004 - Basic Commands

Commands are the most direct and efficient way to communicate with the OS. They are to be entered in the [teminal](#terminal). 

#### **Directories**

Here are presented the most common commands related to the filesystem and directories.

```
# Change working directory to the path.

cd <absolute or relative path>

# Go back to the parent directory.

cd ..

# Go back multiple parent directory (you can do it until you reach the root).

cd ../..

# Go back to previous working directory.

cd -

# Go back to `/home/<user>`.

cd ~

# or

cd 

# Make new directory.
  # Warning: cannot create nested directories.

mkdir <new directory>

# You can create multiples directories.

mkdir dir1 dir2 dir3

# Nested directories

mkdir -p parent/child/1/2/3

mkdir dir1 dir2 dir3

# Print working directory.

pwd

# Remove empty directory

rm -d <directory>

# Remove non-empty directory (and files within)

rm -r <directory>

```

#### **Files**

Here are presented the most common commands related to the files.

```
# Create empty file
  # If file already exists, it does not overwrite it.

touch file.txt 

# Multiple files

touch file1.txt file2.txt

# Creating file with text
  # Warning: if file exists, content is overwritten

echo "hello world!" > file.txt

# Appending text to existing file

echo "more text to be appended" >> file.txt

# Remove file

rm <filename 1> <filename 2>

# Remove all file in directory with extension

rm *.pdf
```

----

### R005 - Vim and Nano

Vim and Nano are both command-line text editors.
Put simply, Nano is the best for beginner, easy to use dans understand. Vim is more powerful, but more complex than Nano.
Nano is known as a WYSIWYG editor, meaning What You See Is What You Get i.e. it's straighforward in its use. Vim is mode-based editor.

You can try and open both editors with `vim` and `nano`. As you can see, Nano has all the useful shortcuts at the bottom of the page while Vim only has its current mode.

#### Modes for Vim

- **Normal (default)**: for navigation. Allow to browse through file.
- **Insert**: for inserting/modifying text. 
  - Press **'i'** to change to insert mode.
- **Command**: for saving/exiting/etc. 
  - Press **':'** to enter command mode.

Press **ESC** to exit a mode (go back to normal).

#### Exit and save

**Nano**:
The shortcut **Ctrl+X** automatically prompts the user to save (or not) the changes. 

**Vim**:
To exit and save in Vim, you must first enter command mode. The command is then `:wq` and press **Enter**.

#### Search

**Nano**:
The shortcut **Ctrl+W** prompts the user to enter string to search for. Use **Alt+W** to skip to onext occurence. 

**Vim**:
To search text in Vim, you must first enter command mode. The search command is then `/<word the be searched>` and press **Enter**.

---

### R006 - Saving terminal output to disk

The accepted answer for this [askubuntu thread](https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file) presents in a neat table all the options to save terminal output to disk. The summary is left here as a useful cheat-sheet.
`
*** Note that n.e means 'not existing'.
```
          || visible in terminal ||   visible in file   || existing
  Syntax  ||  StdOut  |  StdErr  ||  StdOut  |  StdErr  ||   file   
==========++==========+==========++==========+==========++===========
    >     ||    no    |   yes    ||   yes    |    no    || overwrite
    >>    ||    no    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
   2>     ||   yes    |    no    ||    no    |   yes    || overwrite
   2>>    ||   yes    |    no    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
   &>     ||    no    |    no    ||   yes    |   yes    || overwrite
   &>>    ||    no    |    no    ||   yes    |   yes    ||  append
          ||          |          ||          |          ||
 | tee    ||   yes    |   yes    ||   yes    |    no    || overwrite
 | tee -a ||   yes    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    || overwrite
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
|& tee    ||   yes    |   yes    ||   yes    |   yes    || overwrite
|& tee -a ||   yes    |   yes    ||   yes    |   yes    ||  append
```

---

### R007 - SSH (Secure Shell)

The ssh protocol is used to log into remote systems/servers. The most basic example of connecting to a remote host is:
`ssh <remote host>`

Where 'remote host' is an existing IP adress or domain that you will be connecting to. Not that this command assume the same username on both systems. 
When connecting to a remote host with different username, use the syntax:
`ssh <remote username>@<remote host>`

A useful feature of `ssh` is that it can be used to do X11 forwarding. This will forward every windows you open on your remote server to your computer. To enable X11 forwarding, use the syntax: `ssh -Y <remote username>@<remote host>`. Since X11 forwarding can be slow for heavy or extended work, we recommend using [TeamViewer](https://www.teamviewer.com/en-us/download/linux/) in such use cases.

You might be prompted to enter the password. Once it is done, you will see the current shell change to the remote user@remote host. To exit, simply type
`exit`.

### **Using Custom Host Names For Your SSH Connections**

Remembering every device's IP address that you need remote access into can be troublesome. A good way to keep track of those addresses is by writing [aliases](#r000---aliases).

```
# Example of a custom alias

alias alienware="ssh <username>@192.168.0.1"
```

Although this is a prefectly acceptable solution, we recommend using a separate file to store every remote hosts you might want access to.

1. Create a config file inside of your '\~/.ssh' directory
   ```
   mkdir -p ~/.ssh && touch ~/.ssh/config
   ```

2. Adding entries to the '\~/.ssh/config' file
   ```
   Host <Custom Remote access name>
      HostName <IP Adress of the remote server>
      User <Username to access remote server>
   ```
   ```
   # Example of a valid '~/.ssh/config' file

   Host Alienware_GRIIS
     HostName 10.244.54.13
     User guillaume

   Host archVM
     HostName 42.69.42.69
     User McLovin
   ```

You will now be able to remote access into your servers using the `ssh` command as follows:
```
ssh Alienware_GRIIS
```

---

### R008 - SCP (Secure Copy)

The `scp` command can be used to copy files to a remote server securely using ssh. The command uses this syntax: 
```
scp <file 1> <file 2> <file 3> ... <remote username>@<remote server>:<remote path>
```

Here is a real world example of how to use the `scp` command. We will assume that you have set up custom ssh host names as suggested [here](#using-custom-host-names-for-your-ssh-connections).

```
scp cute_cat.png feral_cat.png purrfect_cat.png Alienware_GRIIS:/home/guillaume/Cats/
```

You can also copy an entire directory recursively using the `-r` flag:

```
scp -r my_cats/ Alienware_GRIIS:/home/guillaume/
```

This will result in the copy of the `my_cats` directory on the remote server at `/home/guillaume/my_cats/`

---

### R009 - Using Git 

Git is a version control system developped by Linus Torvalds, a famous Nvidia enthusiast. Git is used to manage different version of files in a project and allows easy contribution between said project.

Git should either be installed by default or your system, otherwise you can install `git` using the git package:
```
sudo apt update && sudo apt install git
```

#### **Getting Started**
In order to use Git you need to set at least a name and email:

```
git config --global user.name  "Marcel Carre"
git config --global user.email "Marcel.m_harcele@example.com"
```
See [here](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) for more information.

---

### R010 - Using Anaconda

Anaconda is the world’s most popular Python distribution platform. It is used to manage virtual environments and distribute python packages. There are 2 main Anaconda products available for individual use:
- Anaconda
- Miniconda

#### **Installing Anaconda**

Anaconda comes with multiples conda packages built-in. This obviously comes in a larger file, but this option should have most of what you would need to get started. You can download Anaconda [here](https://www.anaconda.com/products/individual).


#### **Installing Miniconda**

Alternatively, you can use miniconda. Miniconda only comes with the essential packages. You will need to install the packages you need after the installation. This makes it easier to maintain and is the preferred option by many. We provide a script to install miniconda easily.

```
# Installing Miniconda

sudo apt update && sudo apt install curl && \
curl -o ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
cd ~ && \
chmod +x miniconda.sh && \
bash miniconda.sh
```

After miniconda has been installed, can now safely remove the 'miniconda.sh' file.

```
rm ~/miniconda.sh
```

#### **Creating a Conda Environment**

Conda environment makes managing dependencies easier over multiple projects. It ensures that the version of a package you need in a project will not be affected by another project on your computer that needs a different version of the same package. To create a Conda environment, use the following command:

```
conda create -n <Environment name> python=<python version>
```

```
# Example of a Conda environment

conda create -n MEDomicsTools python=3.8
```

To use your newly created environment, you use the following command:

```
conda active MEDomicsTools
```

Once in your environment, you can install the packages you need with either the `conda` package manager or `pip`.

```
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```

To quit a conda environment, you can use the following command:

```
conda deactivate
```

To completely remove a conda environment, you can use this command:

```
conda env remove -n <Environment name>
```

By default, Anaconda will display in your terminal prompt which conda environment you are currently using. If you are using the recommended [Starship Prompt](#using-a-customized-terminal-prompt), this behavior can be redundant. You can disable Anaconda from showing you the current environment by typing this command:

```
conda config --set changeps1 False
```

### R011 - Recommended Terminal Emulator

We recommend using [Kitty](https://sw.kovidgoyal.net/kitty/) as a terminal emulator. This terminal has a lot of useful features such as:
- Offloading the rendering to the GPU for lower system loads
- Offers minimal latency compared to other terminal emulators
- Supports font ligatures and emoji
- Supports hyperlinks
- Supports Graphicsm with images and animations inside the terminal session
- Highly configurable within it's config file

#### **Installing Kitty**

To install kitty, simply run the following command:
```
sudo apt update && sudo apt install kitty
```
To configure Kitty, a config file should be located at `$HOME/.config/kitty/kitty.conf`. If no config file is present after install, you can copy the existing default one using this command:
```
cp /usr/share/doc/kitty ~/.config/
```
The official documentation for kitty can be acessed [here](https://sw.kovidgoyal.net/kitty/conf/).

#### **Using Kittens**

Kitty has a framework for easily creating terminal programs that make use of its advanced features. These programs are called kittens. Kittens are submodules written in python to extend the functionality of kitty. They can also be used both to create useful standalone programs. Here are some of the most used ones:
```
kitty +kitten icat image.jpeg             # show image in the terminal (needs imagemagick)
kitty +kitten diff file1 file2            # show diff of two files
kitty +kitten clipboard                   # this kitten allows working with clipboard even over ssh
```
The official documentation for kittens can be found [here](https://sw.kovidgoyal.net/kitty/kittens_intro/#kittens).

#### **Terminal Issues with SSH and kitty**
When kitty is used to ssh into a remote that does not have its terminfo, various issues can occur. The solution is normally to copy over the terminfo. Kitty has an ssh kitten to automate exactly this.
```
kitty +kitten ssh user@host
```
You may want to set it as an alias for ssh. Alternatively, if you are still having issues, you can manually change your `$TERM` env variable to something like `xterm_256color`, but this might reduce some of the useful features of kitty.

### R012 - Using Tmux and Alternatives

Running a command detached from the shell session and piping the output to a file.
```
python main.py --options >> output.txt &
```