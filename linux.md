# MEDomicsTools Linux Tips

This document presents some Linux tips and tricks to improve your Linux experience.

## Table of Contents
- [MEDomicsTools Linux Tips](#medomicstools-linux-tips)
  * [Table of Contents](#table-of-contents)
  * [Contributors](#contributors)
  * [Changelog](#changelog)
  * [To-Do](#to-do)
  * [Standard](#standard)
    + [R000 - Aliases](#r000---aliases)
    + [R001 - Terminal](#r001---terminal)
      - [**Overview**](#--overview--)
      - [**Terminal Window**](#--terminal-window--)
      - [**Terminal Tabs**](#--terminal-tabs--)
      - [**Terminal Display**](#--terminal-display--)
      - [**Terminal Input**](#--terminal-input--)
      - [**Pimping the terminal**](#--pimping-the-terminal--)
    + [R002 - Working Directory](#r002---working-directory)
    + [R003 - Absolute and Relative Path](#r003---absolute-and-relative-path)

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
- [ ] vim/nano (Achille)
- [ ] basic commands - Directory
- [ ] basic commands - files
- [ ] advanced - piping commands
- [ ] advanced - bash script
- [ ] Save terminal output to disk (Achille)
- [ ] ssh (Achille)
- [ ] scp (Nicolas)
- [ ] git (Achille)
- [ ] alias + bashrc (Nicolas: add stuff to Simon's part)

## Standard

### R000 - Aliases

Aliases are shorthands that can be created to shorten the length of common Linux terminal commands. In Ubuntu, you can add aliases at the end of the hidden '\~/.bashrc' OR '\~/.bash_aliases' files in the 'Home' directory.

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

#### **Pimping the terminal**

Much like aliases, it is possible to modify the user's '~/.bashrc' file to customize the terminal. The *how* is hard to explain briefly thus we recommend consulting this [guide](https://www.fosslinux.com/21753/how-to-customize-your-ubuntu-terminal-prompt.htm).

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

Here are presented the most common commands related to the filesystem, directories, files and folders manipulations.

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

# Print working directory.

pwd

# Remove file
```



