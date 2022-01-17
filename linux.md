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

## To-Do

- [x] Terminal pimping (check with Guillaume Cléroux) (Achille)
- [x] Paths/filesystem (Achille)
- [x] vim/nano (Achille)
- [x] Save terminal output to disk (Achille)
- [x] ssh (Achille)
- [ ] scp (Nicolas)
- [ ] git (Achille)
- [ ] alias + bashrc (Nicolas: add stuff to Simon's part)

## Standard
---
### R000 - Aliases

Aliases are shorthands that can be created to shorten the length of common Linux terminal commands. In Ubuntu, you can add aliases at the end of the hidden '\~/.bashrc' OR '\~/.bash_aliases' files in the 'Home' directory. Although both are valid options, we recommend creating a separate '\~/.bash_aliases' file and adding this line to your '\~/.bashrc' file to make managing your aliases easier:

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

2. Enabling the Hack Font in your terminal of choice. You can navigate to the preferences menu of your terminal and selecting the \
Hack Nerd Font Complete as your default font.
   
3. Downloading the starship prompt.
   ```
   sudo apt install curl && sh -c "$(curl -fsSL https://starship.rs/install.sh)"
   ```

4. Adding this line at the end of your '\~/.bashrc' file
   ```
   eval "$(starship init bash)"
   ```

5. Alternatively, if you are not a fan of emojis in your terminal prompt, you can replace them with symbols using this command
   ```
   sh -c "cd ~/.config && curl -o starship.toml https://raw.githubusercontent.com/sgiardl/MEDomicsTools/main/custom_files/starship.toml"
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

You might be prompted to enter the password. Once it is done, you will see the current shell change to the remote user@remote host. To exit, simply type
`exit`.