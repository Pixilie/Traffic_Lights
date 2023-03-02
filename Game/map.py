import pygame
import os

# Import game files
import trafficLightFile
import roadFile

def loadMap(map, window):
    """Loads the map

    Args:
        map (str): The map file
        window (pygame.display): The window

    Returns:
        spritesList (list): The list of sprites
        roadList (list): The list of roads
        trafficLightsList (list): The list of traffic lights
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
                        trafficLight = trafficLightFile.trafficLight(x, y, "green") 
                        trafficLightsList.add(trafficLight)
                        spritesList.add(trafficLight)
                    else:
                        pass
                    x += tilesSize
                y += tilesSize
    return spritesList, roadList, trafficLightsList