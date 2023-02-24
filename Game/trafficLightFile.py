import pygame

def trafficLight(x, y):
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

def changeTrafficLightsState(trafficLightsList, green, x, y): #TODO: terminer la fonction pour mettre à jour les listes pour les collisions
    """
    Changes the color of the traffic lights
    :param trafficLightsList: The list of traffic lights
    :param green: If the traffic lights are green or not
    :param x: The x position of the mouse
    :param y: The y position of the mouse
    """
    redTrafficLightsList = pygame.sprite.Group()
    for trafficLights in trafficLightsList:
        if trafficLights.rect.collidepoint(x, y) and green == True:
            trafficLights.image = pygame.image.load("./Game/Assets/Textures/road_redlights.png").convert_alpha()
            green = False
            redTrafficLightsList.add(trafficLights)
        elif trafficLights.rect.collidepoint(x, y) and green == False:
            trafficLights.image = pygame.image.load("./Game/Assets/Textures/road_greenlights.png").convert_alpha()
            green = True
            redTrafficLightsList.remove(trafficLights)
    return redTrafficLightsList