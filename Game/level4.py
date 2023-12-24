# Import librairies
import pygame
from pygame.locals import *
import os
import sys

# Import game files
import Game.gameModules.map as map
import Game.gameModules.carFile as carFile
import Game.gameModules.trafficLightFile as trafficLightFile
import Game.gameModules.levelBackend as levelBackend
import Game.gameModules.textFile as textFile

# Level informations -> Level number, level name, completed, lives, score, cars to pass, cars passed
levelInfos = [4, "Niveau 4", textFile.readData("completed", 4, "./Game/levelsData.json"), 6, textFile.readData("score", 4, "./Game/levelsData.json"), 40, 0]

# Write data in json file
if not (textFile.searchData("level_id", levelInfos[0], "./Game/levelsData.json")):
    textFile.writeData({ "level_id" : levelInfos[0], "score" : 0, "completed" : "Non"}, "./Game/levelsData.json")

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

    # Main window setup
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(f'Traffic Light - {levelName}')
    window.fill(white)

    # Sprites list
    spritesList, roadList, trafficLightsList, carSpawnPointsList, grassList = map.loadMap("./Game/Assets/Maps/map_lvl4.txt", window)
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

        # Spawn the cars
        for carSpawnPoint in carSpawnPointsList:
            carFile.createCars(carSpawnPoint, spritesList, carList, windowWidth, windowHeight, ticks, (3, 4))
            # Check if the cars are stuck
            for car in carList:
                for _car in carList:
                    lives, score = carFile.destroyCarAtSpawn(car, _car, spritesList, carList, carSpawnPoint, windowWidth, windowHeight, lives, score, carFile, explosionList)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                gameLoop = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # Pause the game
                    gameLoop, restart = levelBackend.pause(gameLoop, "pause", level, levelName, lives, score, windowWidth, windowHeight, window, restart)
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                # Update and handle the traffic lights
                for trafficLight in trafficLightsList:
                    trafficLightFile.trafficLightsUpdate(trafficLight, x, y, windowWidth, windowHeight)

        # Update and handle the cars
        for car in carList:
            lives, score = carFile.collisionCars(car, carList, spritesList, explosionList, windowWidth, windowHeight, lives, score)
            carFile.collisionRedLights(car, trafficLightsList)
            carsPassed, score = carFile.update(car, spritesList, carList, carsPassed, score)

        # Update and handle the explosions
        for explosion in explosionList:
            carFile.explosionRemove(explosion, explosionList, spritesList)

        # Check if the level is finished
        gameLoop, restart = levelBackend.isLevelFinished(carsPassed, carsToPass, level, levelName, lives, score, windowWidth, windowHeight, window, gameLoop, restart)
        
        # Check if the level needs to be restarted
        if restart:
            gameLoop = False
            levelFunction()

        # Clear the window
        window.fill(white)
        spritesList.draw(window)

        # Draw the texts
        window.blit(lifeText, (windowWidth*0.002, 0))
        window.blit(scoreText, (windowWidth*0.002, windowHeight*0.03))
        window.blit(carsToPassText, (windowWidth*0.002, windowHeight*0.06))

        # Update the display
        pygame.display.flip()
        clock.tick(24)
        ticks = pygame.time.get_ticks()
    pygame.quit()
