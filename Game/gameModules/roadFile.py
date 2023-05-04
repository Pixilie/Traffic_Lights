import pygame
import os

# Changing working directory
os.chdir('../Traffic_Lights')

def road(x, y, windowWidth, windowHeight):
    """Creates a sprite for a road

    Args:
        x (float): x position on the screen
        y (float): y position on the screen

    Returns:
        road (Sprite): Sprite of the road
    """    
    road = pygame.sprite.Sprite()
    road.image = pygame.image.load("./Game/Assets/Textures/road.png").convert_alpha()
    road.image = pygame.transform.smoothscale(road.image, (windowWidth*0.023, windowWidth*0.023))
    road.rect = road.image.get_rect()
    road.rect.x = x
    road.rect.y = y
    return road

def carSpawn(x, y, windowWidth, windowHeight):
    """Creates a sprite for a road that spawns a car

    Args:
        x (float): x position on the screen
        y (float): y position on the screen

    Returns:
        carSpawn (Sprite): Sprite of the road that spawns a car
    """
    carSpawn = pygame.sprite.Sprite()
    carSpawn.image = pygame.image.load("./Game/Assets/Textures/car_spawn.png").convert_alpha()
    carSpawn.image = pygame.transform.smoothscale(carSpawn.image, (windowWidth*0.023, windowWidth*0.023))
    carSpawn.rect = carSpawn.image.get_rect()
    carSpawn.rect.x = x
    carSpawn.rect.y = y
    carSpawn.lastTick = 0
    carSpawn.delay = 0
    carSpawn.speed = 0
    carSpawn.previousSpeed = 0
    return carSpawn

def grass(x, y, windowWidth, windowHeight):
    """Creates a sprite for a grass
    Args:
        x (float): x position on the screen
        y (float): y position on the screen
        windowWidth (float): Width of the window
        windowHeight (float): Height of the window
    Returns:
        grass (Sprite): Sprite of the grass
    """
    grass = pygame.sprite.Sprite()
    grass.image = pygame.image.load("./Game/Assets/Textures/grass.jpg").convert_alpha()
    grass.image = pygame.transform.smoothscale(grass.image, (windowWidth*0.023, windowWidth*0.023))
    grass.rect = grass.image.get_rect()
    grass.rect.x = x
    grass.rect.y = y
    return grass