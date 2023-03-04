# Import librairies
import pygame
from pygame.locals import *

# Import game files
import map
import carFile
import trafficLightFile
import levelFinished

# Level Information
level = 1  # Level number
levelName = "Niveau 1"  # Level name
levelDescription = "Le premier niveau est un niveau d'initiation. Il vous permettra de vous familiariser avec le jeu. Vous devrez apprendre à gérer les feux de signalisation et à éviter les collisions. Bonne chance !"  # Level description
completed = False  # If the level is completed
lives = 3  # Number of lives
score = 0  # Score of the player
carsToPass = 1  # How many cars the player has to pass to complete the level
carsPassed = 0  # How many cars the player has passed

# Pygame init
pygame.init()

# Variables
screenWidth = pygame.display.Info().current_w
screenHeight = pygame.display.Info().current_h
white = (255, 255, 255)
clock = pygame.time.Clock()
ticks = 0
lastTick = 0

# Main window setup
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(f'Traffic Light - {levelName}')
window.fill(white)

# Sprites list
spritesList, roadList, trafficLightsList = map.loadMap("./Game/Assets/Maps/map_lvl1.txt", window)
redTrafficLightsList = pygame.sprite.Group()
carList = pygame.sprite.Group()
explosionList = pygame.sprite.Group()

# TODO: Musics and sounds
# Event loop
gameLoop = True
while gameLoop:
    
    lastTick = carFile.createCars(0, 20, 1, "right", 3000, ticks, lastTick, spritesList, carList)
    lastTick = carFile.createCars(screenWidth, 120, 2, "left", 1000, ticks, lastTick, spritesList, carList)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            gameLoop = False
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos  # Get the mouse position
            for trafficLight in trafficLightsList:
                trafficLightFile.trafficLightsUpdate(
                    trafficLight, x, y)  # Update the traffic lights

    for car in carList:
        carFile.collisionCars(car, carList, spritesList, explosionList) # Check if the cars collide with each other
        carFile.collisionRedLights(car, trafficLightsList) # Check if the cars collide with the red lights
        carsPassed = carFile.update(car, spritesList, carList, carsPassed)  # Update the cars

    for explosion in explosionList:
        carFile.explosionRemove(explosion, explosionList, spritesList) # Remove the explosion

    gameLoop = levelFinished.isLevelFinished(carsPassed, carsToPass, level, levelName, levelDescription, lives, score, window, gameLoop)  # Check if the level is completed
    map.loadMap("./Game/Assets/Maps/map_lvl1.txt", window)  # Load the map
    window.fill(white)  # Fill the window with white
    spritesList.draw(window)  # Draw the sprites
    pygame.display.flip()  # Update the display
    displayRate = clock.tick(60)  # Limit the display rate to 60 fps
    ticks = pygame.time.get_ticks()
pygame.quit()
