import pygame

def trafficLight(x, y, color):
    """
    Creates a sprite for traffic light
    :param x: The x position of the traffic light
    :param y: The y position of the traffic light
    """
    trafficLights = pygame.sprite.Sprite()
    trafficLights.image = pygame.image.load("./Game/Assets/Textures/road_greenlights_v.png").convert_alpha()
    trafficLights.rect = trafficLights.image.get_rect()
    trafficLights.rect.x = x
    trafficLights.rect.y = y
    trafficLights.color = color
    return trafficLights

def trafficLightsUpdate(trafficLight, x, y):
    """
    Changes the color of the traffic lights
    :param trafficLightsList: The list of traffic lights
    :param green: If the traffic lights are green or not
    :param x: The x position of the mouse
    :param y: The y position of the mouse
    """
    if trafficLight.rect.collidepoint(x, y) and trafficLight.color == "green":
        trafficLight.image = pygame.image.load("./Game/Assets/Textures/road_redlights_v.png").convert_alpha()
        trafficLight.color = "red"
    elif trafficLight.rect.collidepoint(x, y) and trafficLight.color == "red":
        trafficLight.image = pygame.image.load("./Game/Assets/Textures/road_greenlights_v.png").convert_alpha()
        trafficLight.color = "green"
    return trafficLight.color
   