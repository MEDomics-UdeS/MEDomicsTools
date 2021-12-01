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

## To-Do

- [ ] Terminal pimping (check with Guillaume Cléroux) (Achille)
- [ ] Paths/filesystem (Achille)
- [ ] vim/nano (Achille)
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
