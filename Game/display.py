import pygame
import os

# Import game files
import trafficLightFile
import roadFile

def loadMap(map, window):
    """
    Loads and display a map from a text file and returns a list of the map
    :param map: The map to load, must be a text file, and must specify the path from the root directory of the project.
    :param window: The window to draw the map on
    """
    roadList = pygame.sprite.Group()
    spritesList = pygame.sprite.Group()
    trafficLightsList = pygame.sprite.Group()
    tilesSize = 30
    x = 0
    y = 0
    if not os.path.isfile(map):
        print("Map doesn't exist.")
    else:
        with open(map, "rt") as file:
            map_data = file.readlines()
            for line in map_data:
                x = 0
                for symbols in line:
                    if symbols == "R":
                        road = roadFile.road(x, y)
                        roadList.add(road)
                        spritesList.add(road)
                    elif symbols == "g":
                        trafficLight = trafficLightFile.trafficLight(x, y)
                        trafficLightsList.add(trafficLight)
                        spritesList.add(trafficLight)
                    else:
                        pass
                    x += tilesSize
                y += tilesSize
    return spritesList, roadList, trafficLightsList