import pygame

def road(x, y):
    """
    Creates a sprite for a road
    :param x: The x position of the road
    :param y: The y position of the road
    """
    road = pygame.sprite.Sprite()
    road.image = pygame.image.load("./Game/Assets/Textures/road.png").convert_alpha()
    road.rect = road.image.get_rect()
    road.rect.x = x
    road.rect.y = y
    return road

def trafficLights(x, y):
    """
    Creates a sprite for traffic light
    :param x: The x position of the traffic light
    :param y: The y position of the traffic light
    """
    trafficLights = pygame.sprite.Sprite()
    trafficLights.image = pygame.image.load("./Game/Assets/Textures/road_greenlights.png").convert_alpha()
    trafficLights.rect = trafficLights.image.get_rect()
    trafficLights.rect.x = x
    trafficLights.rect.y = y
    return trafficLights

def car(x, y):
    """
    Creates a sprite for a car
    :param x: The x position of the car
    :param y: The y position of the car
    """
    car = pygame.sprite.Sprite()
    car.image = pygame.image.load("./Game/Assets/Textures/car.png").convert_alpha()
    car.rect = car.image.get_rect()
    car.rect.x = x
    car.rect.y = y
    return car