import pygame
import time


def car(x, y, direction, speed):
    """Creates a sprite for a car
    Args:
        x (float): x position on the screen
        y (float): y position on the screen
        direction (str): direction of the car
        speed (float): speed of the car
    Returns:
        car (Sprite): Sprite of the car
    """
    car = pygame.sprite.Sprite()
    if direction == "up":
        car.image = pygame.image.load(
            "./Game/Assets/Textures/car_u.png").convert_alpha()
    elif direction == "down":
        car.image = pygame.image.load(
            "./Game/Assets/Textures/car_d.png").convert_alpha()
    elif direction == "left":
        car.image = pygame.image.load(
            "./Game/Assets/Textures/car_l.png").convert_alpha()
    elif direction == "right":
        car.image = pygame.image.load(
            "./Game/Assets/Textures/car_r.png").convert_alpha()
    car.rect = car.image.get_rect()
    car.rect.x = x
    car.rect.y = y
    car.speed = speed
    car.direction = direction
    car.previousSpeed = speed
    return car


def explosion(x, y):
    """Creates a sprite for an explosion
    Args:
        x (float): x position on the screen
        y (float): y position on the screen
    Returns:
        explosion (Sprite): Sprite of the explosion
    """
    explosion = pygame.sprite.Sprite()
    explosion.image = pygame.image.load(
        "./Game/Assets/Textures/explosion.png").convert_alpha()
    explosion.rect = explosion.image.get_rect()
    explosion.rect.x = x
    explosion.rect.y = y
    explosion.spawnTime = pygame.time.get_ticks()
    return explosion


def update(car, spritesList, carList, carsPassed):
    """Updates the car
    Args:
        car (sprite): The car to update
        spritesList (list): The list of sprites
        carList (list): The list of cars
        carsPassed (int): The number of cars that passed
    Returns:
        carsPassed (int): The number of cars that passed
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
    return carsPassed


def collisionRedLights(car, trafficLightsList):
    """Checks if the car is colliding with a red light
    Args:
        car (sprite): The car to check
        trafficLightsList (list): The list of traffic lights
    """
    for trafficLight in trafficLightsList:
        if trafficLight.color == "red" and trafficLight.rect.collidepoint(car.rect.x, car.rect.y):
            car.speed = 0
        elif trafficLight.color == "green" and trafficLight.rect.collidepoint(car.rect.x, car.rect.y):
            car.speed = car.previousSpeed


def collisionCars(car, carList, spritesList, explosionList):
    """Checks if the car is colliding with another car
    Args:
        car (sprite): The car to check
        carList (list): The list of cars
        spritesList (list): The list of sprites
        explosionList (list): The list of explosions
    """    
    _carList = carList.copy()
    _carList.remove(car)
    for _car in _carList:
        if car.rect.colliderect(_car.rect):
            boom = explosion(car.rect.x, car.rect.y)
            spritesList.add(boom)
            explosionList.add(boom)
            car.kill()
            _car.kill()
            car.remove(carList)
            _car.remove(carList)
            car.remove(spritesList)
            _car.remove(spritesList)


def explosionRemove(explosion, explosionList, spritesList):
    """Removes the explosion from the lists
    Args:
        explosion (sprite): The explosion to remove
        explosionList (list): The list of explosions
        spritesList (list): The list of sprites
    """    
    explosionDelay = 2000
    if pygame.time.get_ticks() - explosionDelay > explosion.spawnTime:
        spritesList.remove(explosion)
        explosionList.remove(explosion)
        explosion.kill()


def createCars(x, y, number, speed, delay, spritesList, carList):  # TODO: finir la fonction
    """Creates a list of cars

    Args:
        x (float): x start position on the screen
        y (float): y start position on the screen
        number (int): number of cars to create
        speed (float): speed of the cars
        delay (int): delay between each car
        spritesList (list): The list of sprites
        carList (list): The list of cars
    """
    nextCarSpawn = 0
    for i in range(number):
        if i == number - 1:
            pass
        else:
            print("Creating car " + str(i) + " of " + str(number))
            if pygame.time.get_ticks() > nextCarSpawn:
                nextCarSpawn += delay
                newCar = car(x, y, "right", speed)
                spritesList.add(newCar)
                carList.add(newCar)
