import pygame

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
    road.image = pygame.transform.smoothscale(road.image, (windowWidth*0.02277, windowWidth*0.02277))
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
    carSpawn.image = pygame.transform.smoothscale(carSpawn.image, (windowWidth*0.02277, windowWidth*0.02277))
    carSpawn.rect = carSpawn.image.get_rect()
    carSpawn.rect.x = x
    carSpawn.rect.y = y
    carSpawn.lastTick = 0
    carSpawn.delay = 0
    carSpawn.speed = 0
    carSpawn.previousSpeed = 0
    return carSpawn