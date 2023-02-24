# Level Information
level = 1 # Level number
levelName = "Niveau 1" # Level name
levelDescription = "Le premier niveau est un niveau d'initiation. Il vous permettra de vous familiariser avec le jeu. Vous devrez apprendre à gérer les feux de signalisation et à éviter les collisions. Bonne chance !" # Level description
completed = False # If the level is completed
lives = 3 # Number of lives
score = 0 # Score of the player
carsToPass = 10 # How many cars the player has to pass to complete the level

# Changing path and import game files
import display
import carFile
import trafficLightFile

# Pygame init
import pygame
from pygame.locals import *
pygame.init()

# Variables
screenWidth = pygame.display.Info().current_w
screenHeight = pygame.display.Info().current_h
white = (255, 255, 255)

# Main window setup
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(f'Traffic Light - {levelName}')
window.fill(white)

# Sprites list
spritesList, roadList, trafficLightsList = display.loadMap("./Game/Assets/Maps/map_lvl1.txt", window)
redTrafficLightsList = pygame.sprite.Group()
carList = pygame.sprite.Group()

clock = pygame.time.Clock()

car = carFile.car(10, 30, 2, 1)
spritesList.add(car)
carList.add(car)

# Event loop
gameLoop = True
green = True
while gameLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameLoop = False
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            trafficLightFile.changeTrafficLightsState(trafficLightsList, green, x, y)
            green = not green      
                
    display.loadMap("./Game/Assets/Maps/map_lvl1.txt", window)
    # spritesList.update() # Inutile
    carFile.update(carList)
    carFile.collisionRedLights(carList, redTrafficLightsList)
    carFile.collisionCars(carList, spritesList)
    window.fill(white)
    spritesList.draw(window)
    pygame.display.flip()
    displayRate = clock.tick(60)
pygame.quit()
