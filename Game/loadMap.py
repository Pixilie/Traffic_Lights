import pygame
import os

def loadMap(map, window):
    """
    Loads and display a map from a text file and returns a list of the map
    :param map: The map to load, must be a text file, and must specify the path from the root directory of the project.
    :param window: The window to draw the map on
    """
    tilesSize = 30
    x = 0
    y = 0
    roadTile = pygame.image.load("./Game/Assets/Textures/road.png").convert_alpha()
    if not os.path.isfile(map):
        print("Map doesn't exist.")
    else:
        with open(map, "rt") as file:
            map_data = file.readlines()
            for line in map_data:
                x = 0
                for symbols in line:
                    if symbols == "r":
                        window.blit(roadTile, (x, y))
                    else:
                        pass
                    x += tilesSize
                y += tilesSize