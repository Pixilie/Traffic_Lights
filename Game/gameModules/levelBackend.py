# Import librairies
import pygame
from pygame.locals import *
import os
import textFile

# Changing working directory
os.chdir('../Traffic_Lights')

def isLevelFinished(carsPassed, carsToPass, level, levelName, lives, score, windowWidth, windowHeight, window, gameLoop, userEvent):
    """Checks if the level is finished
    Args:
        carsPassed (int): The number of cars that passed
        carsToPass (int): The number of cars to pass
        level (int): The level number
        levelName (str): The name of the level
        lives (int): The number of lives
        score (int): The score
        windowWidth (int): The width of the window
        windowHeight (int): The height of the window
        window (pygame.display): The window
        gameLoop (bool): The game loop
        userEvent (pygame.event): Custom event
    Returns:
        gameLoop (bool): The game loop
    """
    if carsPassed == carsToPass or lives == 0:
        if carsPassed == carsToPass:
            textFile.modifyData(level, "completed", "true", "./Game/levelsData.json")
            textFile.modifyData(level, "score", score, "./Game/levelsData.json")
            context = "gagné"
        gameLoop = pause(gameLoop, context, level, levelName, lives, score, windowWidth, windowHeight, window, userEvent)
    else:
        return gameLoop

def pause(gameLoop, context, level, levelName, lives, score, windowWidth, windowHeight, window, userEvent):
    """Pause the game
    Args:
        gameLoop (bool): The game loop
        context (str): The context of the pause
        level (int): The level number
        levelName (str): The name of the level
        lives (int): The number of lives
        score (int): The score
        windowWidth (int): The width of the window
        windowHeight (int): The height of the window
        window (pygame.display): The window
        userEvent (pygame.event): Custom event
    Returns:
        gameLoop (bool): The game loop
    """
    # Draw background
    background = pygame.image.load("./Game/Assets/Textures/pause_background.png")
    scaledBackground = pygame.transform.smoothscale(background, (windowWidth, windowWidth))
    window.blit(scaledBackground, (0, 0))
    pygame.display.update()
    
    if context == "pause":
        pauseWindow(windowWidth, windowHeight, window)
    else:
        finishWindow(level, levelName, lives, score, windowWidth, windowHeight, window, context)

    pause = True
    while pause:
        if context == "pause":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pause = False
                    if event.key == K_ESCAPE:
                        pygame.quit()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = False
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        pygame.event.post(userEvent)
                        pause = False
                    if event.key == K_ESCAPE:
                        pygame.quit()


    gameLoop = not pause
    return gameLoop

#----------------------------------------------
# Windows creation

# TODO: Faire la fenêtre de fin de niveau
def finishWindow(level, levelName, lives, score, windowWidth, windowHeight, window, context):
    """The window that appears when the level is finished
    Args:
        level (int): The level number
        levelName (str): The name of the level
        lives (int): The number of lives
        score (int): The score
        windowWidth (int): The width of the window
        windowHeight (int): The height of the window
        window (pygame.display): The window
        context (str): The context of the pause
    """

    textFile.writeText(windowWidth*0.5, windowHeight*0.05, "Arial", round(windowWidth*0.1), (0, 0, 0), levelName, True, window)
    textFile.writeText(windowWidth*0.5, windowHeight*0.2, "Arial", round(windowWidth*0.05), (0, 0, 0), f"Vous avez {context}", True, window)
    textFile.writeText(windowWidth*0.5, windowHeight*0.4, "Arial", round(windowWidth*0.03), (0, 0, 0), f"Vous aviez {score} points", True, window)
    textFile.writeText(windowWidth*0.5, windowHeight*0.5, "Arial", round(windowWidth*0.03), (0, 0, 0), f"Il vous restait {lives} vies", True, window)
    textFile.writeText(windowWidth*0.5, windowHeight*0.8, "Arial", round(windowWidth*0.03), (0, 0, 0), "Appuyez sur 'R' pour recommencer ou 'Echap' pour retourner au menu", True, window)

def pauseWindow(windowWidth, windowHeight, window):
    """The window that appears when the game is paused
    Args:
        windowWidth (int): The width of the window
        windowHeight (int): The height of the window
        window (pygame.display): The window
    """    
    textFile.writeText(windowWidth*0.5, windowHeight*0.1, "Arial", round(windowWidth*0.05), (0, 0, 0), "Jeu en pause", True, window)
    textFile.writeText(windowWidth*0.5, windowHeight*0.4, "Arial", round(windowWidth*0.03), (0, 0, 0), "Appuyez sur 'Espace' pour continuer ou 'Echap' pour retourner au menu", True, window)