import pygame

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
    car.previousSpeed = speed
    return car
    
def update(carList):
    for car in carList:
        car.rect.x += car.speed

def collisionRedLights(carList, redTrafficLightsList): # FIXME: collision avec les feux rouges marche pas
    for car in carList:
        collideRedTrafficLightsList = pygame.sprite.spritecollide(car, redTrafficLightsList, False)
        print(collideRedTrafficLightsList)
        for car in collideRedTrafficLightsList:
            car.speed = 0

def collisionCars(carList, spriteList):
    collideCarList = []
    for car in carList:
        _carList = carList.copy()
        _carList = _carList.remove(car)
        if _carList != None:
            _collideCarlist = pygame.sprite.spritecollide(car, _carList, False)
            print(_collideCarlist)
            if len(_collideCarlist) > 0:
                collideCarList.append(car)
            for car in collideCarList:
                car.kill()
                spriteList.remove(car)
                carList.remove(car)
