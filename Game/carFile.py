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
    
def update(car, spritesList, carList): # FIXME: Erreur quand on supprime une voiture de la liste on ne peut plus changer la
    width, heigh = pygame.display.get_window_size()
    car.rect.x += car.speed
    '''if car.rect.x > width:
        print("remove")         
        car.kill()
        car.remove(carList)
        car.remove(spritesList)
    if car.rect.y > heigh:
        print("remove")
        car.kill()
        car.remove(carList)
        car.remove(spritesList)'''
    return spritesList, carList

def collisionRedLights(car, trafficLightsList): # TODO: collision avec les feux rouges (refaire)
    return car.speed

def collisionCars(car, carList, spritesList): #FIXME: collision avec les voitures marche pas
    collideCarList = []
    _carList = carList.copy()
    _carList = _carList.remove(car)
    if _carList != None:
        _collideCarList = pygame.sprite.spritecollide(car, _carList, False)
        if len(_collideCarList) > 0:
            collideCarList.append(car)
        for car in collideCarList:
            car.kill()
            spritesList.remove(car)
            carList.remove(car)
    return carList, spritesList
