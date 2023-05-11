import pygame
import time
import random
import os
import soundsFile

# Changing working directory
os.chdir('../Traffic_Lights')

def car(x, y, direction, speed, windowWidth, windowHeight):
    """Creates a sprite for a car
    Args:
        x (float): x position on the screen
        y (float): y position on the screen
        direction (str): direction of the car
        speed (float): speed of the car
    Returns:
        car (Sprite): Sprite of the car
    """
    # Play the car horn sound
    soundsFile.playSound("sound", soundsFile.getVolume(), "./Game/Assets/Sounds/car-horn.mp3")

    # Creating the car sprite
    car = pygame.sprite.Sprite()

    # Loading the car image
    colorInt = random.randint(1, 5)
    if colorInt == 1:
        color = "b"
    elif colorInt == 2:
        color = "g"
    elif colorInt == 3:
        color = "r"
    elif colorInt == 4:
        color = "y"
    else:
        color = "gr"

    if direction == "up":
        car.image = pygame.image.load(
            f"./Game/Assets/Textures/{color}car_u.png").convert_alpha()
    elif direction == "down":
        car.image = pygame.image.load(
            f"./Game/Assets/Textures/{color}car_d.png").convert_alpha()
    elif direction == "left":
        car.image = pygame.image.load(
            f"./Game/Assets/Textures/{color}car_l.png").convert_alpha()
    elif direction == "right":
        car.image = pygame.image.load(
            f"./Game/Assets/Textures/{color}car_r.png").convert_alpha()
    car.image = pygame.transform.smoothscale(car.image, (windowWidth*0.02277, windowWidth*0.02277))

    # Setting the car's rect
    car.rect = car.image.get_rect()
    car.rect.x = x
    car.rect.y = y

    # Setting the car's attributes
    car.speed = speed
    car.direction = direction
    car.previousSpeed = speed
    car.stopped = False
    return car

def explosion(x, y, windowWidth, windowHeight):
    """Creates a sprite for an explosion
    Args:
        x (float): x position on the screen
        y (float): y position on the screen
    Returns:
        explosion (Sprite): Sprite of the explosion
    """
    soundsFile.playSound("sound", soundsFile.getVolume(), "./Game/Assets/Sounds/explosion.mp3")
    explosion = pygame.sprite.Sprite()
    explosion.image = pygame.image.load("./Game/Assets/Textures/explosion.png").convert_alpha()
    explosion.image = pygame.transform.smoothscale(explosion.image, (windowWidth*0.02277, windowWidth*0.02277))
    explosion.rect = explosion.image.get_rect()
    explosion.rect.x = x
    explosion.rect.y = y
    explosion.spawnTime = pygame.time.get_ticks()
    return explosion

def update(car, spritesList, carList, carsPassed, score):
    """Updates the car
    Args:
        car (sprite): The car to update
        spritesList (list): The list of sprites
        carList (list): The list of cars
        carsPassed (int): The number of cars that passed
    Returns:
        
    """
    width, heigh = pygame.display.get_window_size()
    if car.direction == "up":
        car.rect.y -= car.speed
    elif car.direction == "down":
        car.rect.y += car.speed
    elif car.direction == "left":
        car.rect.x -= car.speed
    else:
        car.rect.x += car.speed
    if car.rect.x > width or car.rect.x < 0 or car.rect.y > heigh or car.rect.y < 0:
        car.kill()
        car.remove(carList)
        car.remove(spritesList)
        carsPassed += 1
        score += 100

    return carsPassed, score

def collisionRedLights(car, trafficLightsList):
    """Checks if the car is colliding with a red light
    Args:
        car (sprite): The car to check
        trafficLightsList (list): The list of traffic lights
    """
    for trafficLight in trafficLightsList:
        if trafficLight.color == "red" and trafficLight.rect.collidepoint(car.rect.x, car.rect.y):
            car.speed = 0
            car.stopped = True
        elif trafficLight.color == "green" and trafficLight.rect.collidepoint(car.rect.x, car.rect.y):
            if car.stopped:
                car.speed = car.previousSpeed
                car.stopped = False
            else:
                car.stopped = False

def collisionCars(car, carList, spritesList, explosionList, windowWidth, windowHeight, lives, score):
    """Checks if the car is colliding with another car and handles the collision
    Args:
        car (sprite): The car to check
        carList (list): The list of cars
        spritesList (list): The list of sprites
        explosionList (list): The list of explosions
    """
    # Get the position of the new car
    carPos = car.rect.copy()

    # Remove the new car from the car list
    carList.remove(car)

    for _car in carList:
        if carPos.colliderect(_car.rect):
            if car.direction == _car.direction:
                if (_car.speed != 0 or _car.stopped == False) and (not(car.stopped and _car.stopped and car.rect.colliderect(_car.rect))):
                    _car.speed = car.speed
                    _car.stopped = False
                elif (_car.speed == 0 or _car.stopped == True):
                    _car.stopped = True
                    car.speed = 0
                    car.stopped = True
                    if _car.previousSpeed >= car.previousSpeed:
                        _car.previousSpeed = car.previousSpeed
            else:
                boom = explosion(car.rect.x, car.rect.y, windowWidth, windowHeight)
                spritesList.add(boom)
                explosionList.add(boom)
                car.kill()
                _car.kill()
                carList.remove(car)
                carList.remove(_car)
                spritesList.remove(car)
                spritesList.remove(_car)
                lives -= 1
                score -= 50

        if car.direction == "up":
            xPos = 0
            yPos = -windowWidth*0.032
        elif car.direction == "down":
            xPos = 0
            yPos = windowWidth*0.032
        elif car.direction == "left":
            xPos = -windowWidth*0.032
            yPos = 0
        else:
            xPos = windowWidth*0.032
            yPos = 0

        if (car.stopped == True) and (_car.rect.collidepoint(carPos.x + xPos, carPos.y + yPos)):
            car.speed = 0
            car.stopped = True
        else:
            car.speed = car.previousSpeed
            car.stopped = False            

    carList.add(car)

    for _car in carList: 
        if car != _car:
            if _car.rect.collidepoint(carPos.x + xPos, carPos.y + yPos):
                if car.direction == _car.direction:
                    if car.stopped == False or car.speed != 0:
                        car.speed = _car.speed
    return lives, score

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

def createCars(carSpawnPoint, spritesList, carList, windowWidth, windowHeight, ticks, speedRange):
    """Creates a car

    Args:
        carSpawnPoint (sprites): Spawn point of the car
        spritesList (List of sprites): List of sprites
        carList (List of sprites): List of cars
        windowWidth (int): Width of the window
        windowHeight (int): Height of the window
        ticks (int): Number of ticks
        speedRange (tuple): Speed for the cars
    """    
    if ticks > carSpawnPoint.lastTick + carSpawnPoint.delay:
        min , max = speedRange
        if 0 <= carSpawnPoint.rect.x <= windowWidth*0.023:
            min, max = speedRange
            speed = random.randint(min, max)
            newCar = car(carSpawnPoint.rect.x, carSpawnPoint.rect.y, "right", speed, windowWidth, windowHeight)
            newCar.add(spritesList)
            newCar.add(carList)
            carSpawnPoint.lastTick = ticks
            carSpawnPoint.delay = random.randint(5000, 20000)
        
        if windowWidth - windowWidth*0.023 <= carSpawnPoint.rect.x <= windowWidth:
            min, max = speedRange
            speed = random.randint(min, max)
            newCar = car(carSpawnPoint.rect.x, carSpawnPoint.rect.y, "left", speed, windowWidth, windowHeight)
            newCar.add(spritesList)
            newCar.add(carList)
            carSpawnPoint.lastTick = ticks
            carSpawnPoint.delay = random.randint(5000, 20000)
        
        if 0 <= carSpawnPoint.rect.y <= windowWidth*0.023:
            min, max = speedRange
            speed = random.randint(min, max)
            newCar = car(carSpawnPoint.rect.x, carSpawnPoint.rect.y, "down", speed, windowWidth, windowHeight)
            newCar.add(spritesList)
            newCar.add(carList)
            carSpawnPoint.lastTick = ticks
            carSpawnPoint.delay = random.randint(5000, 20000)
        
        if windowHeight - windowWidth*0.023 <= carSpawnPoint.rect.y <= windowHeight:
            min, max = speedRange
            speed = random.randint(min, max)
            newCar = car(carSpawnPoint.rect.x, carSpawnPoint.rect.y, "up", speed, windowWidth, windowHeight)
            newCar.add(spritesList)
            newCar.add(carList)
            carSpawnPoint.lastTick = ticks
            carSpawnPoint.delay = random.randint(5000, 20000)