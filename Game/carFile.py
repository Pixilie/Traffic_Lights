import pygame

def car(x, y, direction, speed):
    """
    Creates a sprite for a car
    :param x: The x position of the car
    :param y: The y position of the car
    """
    car = pygame.sprite.Sprite()
    car.image = pygame.image.load("./Game/Assets/Textures/car_r.png").convert_alpha()
    car.rect = car.image.get_rect()
    car.rect.x = x
    car.rect.y = y
    car.speed = speed
    car.direction = direction
    car.previousSpeed = speed
    return car

def explosion(x, y):
    """
    Creates a sprite for an explosion
    :param x: The x position of the explosion
    :param y: The y position of the explosion
    """
    explosion = pygame.sprite.Sprite()
    explosion.image = pygame.image.load("./Game/Assets/Textures/explosion.png").convert_alpha()
    explosion.rect = explosion.image.get_rect()
    explosion.rect.x = x
    explosion.rect.y = y
    return explosion
    
def update(car, spritesList, carList, carsPassed):
    """
    Updates the car
    :param car: The car to update
    :param spritesList: The list of sprites
    :param carList: The list of cars
    """
    width, heigh = pygame.display.get_window_size()
    car.rect.x += car.speed
    if car.rect.x > width:
        car.kill()
        car.remove(carList)
        car.remove(spritesList)
        carsPassed += 1
    if car.rect.y > heigh:
        car.kill()
        car.remove(carList)
        car.remove(spritesList)
        carsPassed += 1

def collisionRedLights(car, trafficLightsList):
    """
    Checks if the car is colliding with a red light
    :param car: The car to check
    :param trafficLightsList: The list of traffic lights
    """
    for trafficLight in trafficLightsList:
        if trafficLight.color == "red" and trafficLight.rect.collidepoint(car.rect.x, car.rect.y):
            car.speed = 0
        elif trafficLight.color == "green" and trafficLight.rect.collidepoint(car.rect.x, car.rect.y):
            car.speed = car.previousSpeed

def collisionCars(car, carList, spritesList):
    """
    Checks if the car is colliding with another car
    :param car: The car to check
    :param carList: The list of cars
    :param spritesList: The list of sprites
    """
    _carList = carList.copy()
    _carList.remove(car)
    for _car in _carList:
        if car.rect.colliderect(_car.rect):
            boom = explosion(car.rect.x, car.rect.y)
            spritesList.add(boom) #TODO: Remove the explosion after a while
            car.kill()
            _car.kill()
            car.remove(carList)
            _car.remove(carList)
            car.remove(spritesList)
            _car.remove(spritesList)
       
