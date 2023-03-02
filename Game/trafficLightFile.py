import pygame

def trafficLight(x, y, color):
    """Creates a sprite for a traffic light
    Args:
        x (float): position on the screen
        y (float): position on the screen
        color (str): The color of the traffic light
    Returns:
        trafficLight (Sprite): Sprite of the traffic light
    """    
    trafficLights = pygame.sprite.Sprite()
    trafficLights.image = pygame.image.load("./Game/Assets/Textures/road_greenlights_v.png").convert_alpha()
    trafficLights.rect = trafficLights.image.get_rect()
    trafficLights.rect.x = x
    trafficLights.rect.y = y
    trafficLights.color = color
    return trafficLights

def trafficLightsUpdate(trafficLight, x, y):
    """Updates the traffic light
    Args:
        trafficLight (sprite): The traffic light to update
        x (float): position on the screen
        y (float): position on the screen
    Returns:
        trafficLight.color (str): The color of the traffic light
    """    
    if trafficLight.rect.collidepoint(x, y) and trafficLight.color == "green":
        trafficLight.image = pygame.image.load("./Game/Assets/Textures/road_redlights_v.png").convert_alpha()
        trafficLight.color = "red"
    elif trafficLight.rect.collidepoint(x, y) and trafficLight.color == "red":
        trafficLight.image = pygame.image.load("./Game/Assets/Textures/road_greenlights_v.png").convert_alpha()
        trafficLight.color = "green"
    return trafficLight.color
   