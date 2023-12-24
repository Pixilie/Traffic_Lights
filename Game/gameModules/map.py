import pygame
import os

# Import game files
import Game.gameModules.trafficLightFile as trafficLightFile
import Game.gameModules.roadFile as roadFile

def loadMap(map, window):
    """Loads the map
    Args:
        map (str): The map file
        window (pygame.display): The window
    Returns:
        spritesList (list): The list of sprites
        roadList (list): The list of roads
        trafficLightsList (list): The list of traffic lights
        carSpawnPointsList (list): The list of car spawn points
        grassList (list): The list of grass
    """    
    roadList = pygame.sprite.Group()
    spritesList = pygame.sprite.Group()
    trafficLightsList = pygame.sprite.Group()
    carSpawnPointsList = pygame.sprite.Group()
    grassList = pygame.sprite.Group()
    
    windowSize = pygame.display.get_surface()
    windowWidth, windowHeight = windowSize.get_width(), windowSize.get_height()
    
    tilesSize = round(windowWidth*0.02273)
    x = 0
    y = 0
    if not os.path.isfile(map):
        print("Map doesn't exist.")
        pass
    else:
        with open(map, "rt") as file:
            map_data = file.readlines()
            for line in map_data:
                x = 0
                for symbols in line:
                    if symbols == "R":
                        road = roadFile.road(x, y, window.get_width(), window.get_height())
                        roadList.add(road)
                        spritesList.add(road)
                    elif symbols == "g":
                        trafficLight = trafficLightFile.trafficLight(x, y, "green", window.get_width(), window.get_height()) 
                        trafficLightsList.add(trafficLight)
                        spritesList.add(trafficLight)
                    elif symbols == "c":
                        carSpawn = roadFile.carSpawn(x, y, window.get_width(), window.get_height())
                        carSpawnPointsList.add(carSpawn)
                        spritesList.add(carSpawn)
                    else:
                        grass = roadFile.grass(x, y, window.get_width(), window.get_height())
                        grassList.add(grass)
                        spritesList.add(grass)
                    x += tilesSize
                y += tilesSize
    return spritesList, roadList, trafficLightsList, carSpawnPointsList, grassList
