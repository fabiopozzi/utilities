#!/usr/bin/env python3
"""
cambia_sfondo: find and change desktop background.
"""
import os
import random
import subprocess

wallpaper_dir = "/home/fabio/Pictures/Wallpapers/"

def main():
    """ main function """
    file_list = os.listdir(wallpaper_dir)
    nuovo_sfondo = random.choice(file_list)
    path_sfondo = os.path.join(wallpaper_dir, nuovo_sfondo)
    print(path_sfondo)
    lista_parametri = ["gsettings", "set", "org.gnome.desktop.background",
    "picture-uri", path_sfondo]
    subprocess.run(lista_parametri)


if __name__ == '__main__':
    main()


