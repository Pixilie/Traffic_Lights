import pygame
import os

# Import game files
import sprites

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
                        road = sprites.road(x, y)
                        roadList.add(road)
                        spritesList.add(road)
                    elif symbols == "g":
                        trafficLights = sprites.trafficLights(x, y)
                        trafficLightsList.add(trafficLights)
                        spritesList.add(trafficLights)
                    else:
                        pass
                    x += tilesSize
                y += tilesSize
    return spritesList, roadList, trafficLightsList

def changeTrafficLightsState(trafficLightsList, green, x, y): #TODO: terminer la fonction pour mettre à jour les listes pour les collisions
    """
    Changes the color of the traffic lights
    :param trafficLightsList: The list of traffic lights
    :param green: If the traffic lights are green or not
    :param x: The x position of the mouse
    :param y: The y position of the mouse
    """
    for trafficLights in trafficLightsList:
        if trafficLights.rect.collidepoint(x, y) and green == True:
            trafficLights.image = pygame.image.load("./Game/Assets/Textures/road_redlights.png").convert_alpha()
            green = False
        elif trafficLights.rect.collidepoint(x, y) and green == False:
            trafficLights.image = pygame.image.load("./Game/Assets/Textures/road_greenlights.png").convert_alpha()
            green = True 