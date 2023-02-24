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