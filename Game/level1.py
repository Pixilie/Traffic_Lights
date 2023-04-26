# Import librairies
import pygame
from pygame.locals import *
import os
import sys

# Changing working directory
os.chdir('../Traffic_Lights')
sys.path.append(f'{os.getcwd()}\\Game')

# Import game files
import map
import carFile
import trafficLightFile
import levelFinished

# Level informations
levelInfos = [1, "Niveau 1", False, 3, 0, 100, 0]  # List of level information

def level():
    """Launch the level."""

    # Pygame init
    pygame.init()

    # Variables
    windowWidth = pygame.display.Info().current_w
    windowHeight = pygame.display.Info().current_h
    white = (255, 255, 255)
    clock = pygame.time.Clock()
    ticks = 0
    lastTick = 0
    level, levelName, completed, lives, score, carsToPass, carsPassed = levelInfos

    # Main window setup
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(f'Traffic Light - {levelName}')
    window.fill(white)

    # Sprites list
    spritesList, roadList, trafficLightsList, carSpawnPointsList = map.loadMap("./Game/Assets/Maps/test.txt", window)
    redTrafficLightsList = pygame.sprite.Group()
    carList = pygame.sprite.Group()
    explosionList = pygame.sprite.Group()

    # TODO: Musics and sounds
    # Event loop
    gameLoop = True
    while gameLoop:
        for carSpawnPoint in carSpawnPointsList:
            carFile.createCars(carSpawnPoint, spritesList, carList, windowWidth, windowHeight, ticks, 1) # Create the cars
        
        for event in pygame.event.get():
            if event.type == QUIT:
                gameLoop = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    gameLoop = False #TODO: Add a pause menu
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos  # Get the mouse position
                for trafficLight in trafficLightsList:
                    trafficLightFile.trafficLightsUpdate(trafficLight, x, y, windowWidth, windowHeight)  # Update the traffic lights

        for car in carList:
            carFile.collisionCars(car, carList, spritesList, explosionList, windowWidth, windowHeight, lives) # Check if the cars collide with each other
            carFile.collisionRedLights(car, trafficLightsList) # Check if the cars collide with the red lights
            carsPassed = carFile.update(car, spritesList, carList, carsPassed)  # Update the cars

        for explosion in explosionList:
            carFile.explosionRemove(explosion, explosionList, spritesList) # Remove the explosion

        gameLoop = levelFinished.isLevelFinished(carsPassed, carsToPass, level, levelName, lives, score, window, gameLoop)  # Check if the level is completed
        map.loadMap("./Game/Assets/Maps/map_lvl1.txt", window)  # Load the map
        window.fill(white)  # Fill the window with white
        spritesList.draw(window)  # Draw the sprites
        pygame.display.flip()  # Update the display
        displayRate = clock.tick(60)  # Limit the display rate to 60 fps
        ticks = pygame.time.get_ticks()
    pygame.quit()
