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
        color = "g" # A remplacer par b
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
    car.last_collision_time = 0
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
        if car.rect.colliderect(_car.rect): #Si elles se touchent
            if car.stopped or _car.stopped == True: #Si l'une des deux est arrêtée
                _car.speed = 0
                car.speed = 0
                _car.stopped = True
                car.stopped = True
                car.last_collision_time = time.time()
            elif _car.direction == car.direction: #Si elles vont dans le même sens
                _car.speed = car.speed
            else: #Si elles vont dans des sens opposés
                boom = explosion(car.rect.x, car.rect.y, windowWidth, windowHeight)
                spritesList.add(boom)
                explosionList.add(boom)
                car.kill()
                _car.kill()
                car.remove(carList)
                _car.remove(carList)
                car.remove(spritesList)
                _car.remove(spritesList)
                lives -= 1
                score -= 50                      
    return lives, score
    
def regainSpeed(car, carList):
    """Regains speed for all cars that the given car is colliding with
    Args:
        car (sprite): The car to check
        carList (list): The list of cars
    """  
    current_time = time.time()
    if car.speed != 0 :
        for _car in carList:
            if _car != car:   
                if current_time - _car.last_collision_time <= 5: #Si la collision a eu lieu il y a moins de 5 secondes
                    if car.speed > 1 : #Si la voiture va à plus de 1 pixel par seconde
                        _car.speed = car.speed #On lui donne la vitesse de l'autre voiture
                        _car.stopped = False #On la démarre
                    elif car.speed == 0 or _car.speed == 0 : #Si l'une des deux voitures est arrêtée
                        _car.speed = 0 #On arrête l'autre voiture
                    else: #Si la voiture va à moins de 1 pixel par seconde
                        _car.speed = car.speed #On lui donne la vitesse de l'autre voiture
                        _car.stopped = False #On la démarre

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

def createCars(carSpawnPoint, spritesList, carList, windowWidth, windowHeight, ticks, speed):
    """Creates a car

    Args:
        carSpawnPoint (sprites): Spawn point of the car
        spritesList (List of sprites): List of sprites
        carList (List of sprites): List of cars
        windowWidth (int): Width of the window
        windowHeight (int): Height of the window
        ticks (int): Number of ticks
        speed (int): Speed of the car
    """    
    lastTick = 0
    if ticks > carSpawnPoint.lastTick + carSpawnPoint.delay:
        
        if 0 <= carSpawnPoint.rect.x <= windowWidth*0.023:
            speed = random.randint(1, 3)
            newCar = car(carSpawnPoint.rect.x, carSpawnPoint.rect.y, "right", speed, windowWidth, windowHeight)
            newCar.add(spritesList)
            newCar.add(carList)
            carSpawnPoint.lastTick = ticks
            carSpawnPoint.delay = delay = random.randint(5000, 20000)
        
        if windowWidth - windowWidth*0.023 <= carSpawnPoint.rect.x <= windowWidth:
            speed = random.randint(1, 3)
            newCar = car(carSpawnPoint.rect.x, carSpawnPoint.rect.y, "left", speed, windowWidth, windowHeight)
            newCar.add(spritesList)
            newCar.add(carList)
            carSpawnPoint.lastTick = ticks
            carSpawnPoint.delay = delay = random.randint(5000, 20000)
        
        if 0 <= carSpawnPoint.rect.y <= windowWidth*0.023:
            speed = random.randint(1, 3)
            newCar = car(carSpawnPoint.rect.x, carSpawnPoint.rect.y, "down", speed, windowWidth, windowHeight)
            newCar.add(spritesList)
            newCar.add(carList)
            carSpawnPoint.lastTick = ticks
            carSpawnPoint.delay = delay = random.randint(5000, 20000)
        
        if windowHeight - windowWidth*0.023 <= carSpawnPoint.rect.y <= windowHeight:
            speed = random.randint(1, 3)
            newCar = car(carSpawnPoint.rect.x, carSpawnPoint.rect.y, "up", speed, windowWidth, windowHeight)
            newCar.add(spritesList)
            newCar.add(carList)
            carSpawnPoint.lastTick = ticks
            carSpawnPoint.delay = delay = random.randint(5000, 20000)