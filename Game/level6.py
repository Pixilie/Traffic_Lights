
# Import librairies
import pygame
from pygame.locals import *
import os
import sys

# Changing working directory & adding path
os.chdir('../Traffic_Lights')
sys.path.append(f'{os.getcwd()}\\Game\\gameModules')
sys.path.append(f'{os.getcwd()}\\Game')

# Import game files
import gameModules.map as map
import gameModules.carFile as carFile
import gameModules.trafficLightFile as trafficLightFile
import gameModules.levelBackend as levelBackend
import gameModules.textFile as textFile

# Level informations -> Level number, level name, completed, lives, score, cars to pass, cars passed
levelInfos = [6, "Niveau Final", textFile.readData("completed", 1, "./Game/levelsData.json"),10 , textFile.readData("score", 1, "./Game/levelsData.json"), 60, 0]

# Write data in json file
if not (textFile.searchData("level_id", levelInfos[0], "./Game/levelsData.json")):
    textFile.writeData({ "level_id" : levelInfos[0], "score" : 0, "completed" : "false"}, "./Game/levelsData.json")

def levelFunction():
    """Launch the level."""

    # Pygame initialization
    pygame.init()
    pygame.font.init()

    # Variables
    windowWidth = pygame.display.Info().current_w
    windowHeight = pygame.display.Info().current_h
    white = (255, 255, 255)
    clock = pygame.time.Clock()
    ticks = 0
    level, levelName, completed, lives, score, carsToPass, carsPassed = levelInfos
    restart = False
    developerMode = True

    # Main window setup
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(f'Traffic Light - {levelName}')
    window.fill(white)

    # Sprites list
    spritesList, roadList, trafficLightsList, carSpawnPointsList, grassList = map.loadMap("./Game/Assets/Maps/map_lvl6.txt", window)
    carList = pygame.sprite.Group()
    explosionList = pygame.sprite.Group()

    # Texts
    font = pygame.font.SysFont("Arial", 22)
    lifeText = textFile.writeText(windowWidth*0.002, 0, "Arial", 22, (0, 0, 0), f"Vie(s): {lives}", False, window)
    scoreText = textFile.writeText(windowWidth*0.002, windowHeight*0.03, "Arial", 22, (0, 0, 0), f"Score: {score}", False, window)
    carsToPassText = textFile.writeText(windowWidth*0.002, windowHeight*0.06, "Arial", 22, (0, 0, 0), f"Voiture(s) à faire passer: {carsToPass-carsPassed}", False, window)

    # Event loop & level's code
    gameLoop = True
    while gameLoop:

        # Update the texts
        lifeText = font.render(f"Vie(s): {lives}", True, (0, 0, 0))
        scoreText = font.render(f"Score: {score}", True, (0, 0, 0))
        carsToPassText = font.render(f"Voiture(s) à faire passer: {carsToPass-carsPassed}", True, (0, 0, 0))

        for carSpawnPoint in carSpawnPointsList:
            carFile.createCars(carSpawnPoint, spritesList, carList, windowWidth, windowHeight, ticks, 1) # Create the cars
        
        for event in pygame.event.get():
            if event.type == QUIT:
                gameLoop = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    gameLoop, restart = levelBackend.pause(gameLoop, "pause", level, levelName, lives, score, windowWidth, windowHeight, window, restart)
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos  # Get the mouse position
                for trafficLight in trafficLightsList:
                    trafficLightFile.trafficLightsUpdate(trafficLight, x, y, windowWidth, windowHeight)  # Update the traffic lights

        for car in carList:
            lives, score = carFile.collisionCars(car, carList, spritesList, explosionList, windowWidth, windowHeight, lives, score) # Check if the cars collide with each other
            carFile.collisionRedLights(car, trafficLightsList) # Check if the cars collide with the red lights
            carsPassed, score = carFile.update(car, spritesList, carList, carsPassed, score)  # Update the cars

        for explosion in explosionList:
            carFile.explosionRemove(explosion, explosionList, spritesList) # Remove the explosion

        gameLoop, restart = levelBackend.isLevelFinished(carsPassed, carsToPass, level, levelName, lives, score, windowWidth, windowHeight, window, gameLoop, restart)  # Check if the level is completed

        if restart:  # Check if the level needs to be restarted
            gameLoop = False
            levelFunction()

        window.fill(white)  # Fill the window with white
        spritesList.draw(window)  # Draw the sprites

        # Draw the texts
        window.blit(lifeText, (windowWidth*0.002, 0))
        window.blit(scoreText, (windowWidth*0.002, windowHeight*0.03))
        window.blit(carsToPassText, (windowWidth*0.002, windowHeight*0.06))

        pygame.display.flip()  # Update the display
        clock.tick(24)  # Limit the number of actions
        ticks = pygame.time.get_ticks() # Get the ticks
    pygame.quit()