import pygame

def trafficLight(x, y, color, windowWidth, windowHeight):
    """Creates a sprite for a traffic light
    Args:
        x (float): position on the screen
        y (float): position on the screen
        color (str): The color of the traffic light
    Returns:
        trafficLight (Sprite): Sprite of the traffic light
    """    
    trafficLights = pygame.sprite.Sprite()
    trafficLights.image = pygame.image.load("./Game/Assets/Textures/road_greenlights.png").convert_alpha()
    trafficLights.image = pygame.transform.smoothscale(trafficLights.image, (windowWidth*0.02277, windowWidth*0.02277))
    trafficLights.rect = trafficLights.image.get_rect()
    trafficLights.rect.x = x
    trafficLights.rect.y = y
    trafficLights.color = color
    return trafficLights

def trafficLightsUpdate(trafficLight, x, y, windowWidth, windowHeight):
    """Updates the traffic light
    Args:
        trafficLight (sprite): The traffic light to update
        x (float): position on the screen
        y (float): position on the screen
    Returns:
        trafficLight.color (str): The color of the traffic light
    """    
    if trafficLight.rect.collidepoint(x, y) and trafficLight.color == "green":
        trafficLight.image = pygame.image.load("./Game/Assets/Textures/road_redlights.png").convert_alpha()
        trafficLight.image = pygame.transform.smoothscale(trafficLight.image, (windowWidth*0.02277, windowWidth*0.02277))
        trafficLight.color = "red"
    elif trafficLight.rect.collidepoint(x, y) and trafficLight.color == "red":
        trafficLight.image = pygame.image.load("./Game/Assets/Textures/road_greenlights.png").convert_alpha()
        trafficLight.image = pygame.transform.smoothscale(trafficLight.image, (windowWidth*0.02277, windowWidth*0.02277))
        trafficLight.color = "green"
    return trafficLight.color
   