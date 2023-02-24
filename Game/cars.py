import pygame
import sprites
import display

def car(x, y, direction, speed):
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
    car.speed = speed
    car.direction = direction
    return car
    
def update(carList):
    for car in carList:
        car.rect.x += car.speed


    

def collisions(carList, redTrafficLightsList, spriteList):
    for car in carList:
        collideCarList = pygame.sprite.spritecollide(car, carList)
        collideRedTrafficLightsList = pygame.sprite.spritecollide(car, redTrafficLightsList)
    for car in collideRedTrafficLightsList: # FIXME: Variable referenced before assignment
        car.speed = 0
    for car in collideCarList:
        carList.remove(car)
        spriteList.remove(car)
        car.destroy()