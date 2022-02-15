#!/usr/bin/python3

import os
import subprocess as sp
import shlex

APP_DICT = {
    "Builds": "build-essential curl docker",
    "Fonts": "fonts-firacode fonts-hack",
    "Image Viewer": "gimp",
    "Nvidia": "",
    "Office Suite": "libreoffice-fresh",
    "Terminal": "htop kitty neofetch",
    "Utils": "caffeine cmatrix"
}

def install_nvidia_drivers():
    raise NotImplementedError


if __name__ == "__main__":
    print(
    """
    ===============================================================================
    =                                                                             =
    =                   MEDomicsTools environment setup utility                   =
    =                                                                             =
    ===============================================================================
    
    This script will install the complete set of tools necessary for development
    in the MEDomics Lab. 
    """)
    # sp.call(shlex.split("sudo apt update"))

    install_nvidia_drivers()
