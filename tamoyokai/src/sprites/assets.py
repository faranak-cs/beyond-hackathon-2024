from os import walk
from os.path import join

import pygame


def folder_importer(*path):
    surfs = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            full_path = join(folder_path, file_name)
            surfs[file_name.split('.')[0]] = pygame.image.load(full_path).convert_alpha()
    return surfs

class AssetLoader:

    def __init__(self):
        self.tomoyokai_anims = folder_importer("..", "resources", "animations")
