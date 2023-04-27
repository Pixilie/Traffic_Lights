# Import librairies
import pygame
from pygame.locals import *
import os
import textFile

# Changing working directory
os.chdir('../Traffic_Lights')

def isLevelFinished(carsPassed, carsToPass, level, levelName, lives, score, window, gameLoop):
    """Checks if the level is finished
    Args:
        carsPassed (int): The number of cars that passed
        carsToPass (int): The number of cars to pass
        level (int): The level number
        levelName (str): The name of the level
        lives (int): The number of lives
        score (int): The score
        window (pygame.display): The window
        gameLoop (bool): The game loop
    Returns:
        gameLoop (bool): The game loop
    """
    if carsPassed == carsToPass or lives == 0:
        gameLoop = not gameLoop
        finishWindow(level, levelName, lives, score, window)
    else:
        return gameLoop

# TODO: Faire la fenêtre de fin de niveau
def finishWindow(level, levelName, lives, score, window):
    """The window that appears when the level is finished
    Args:
        level (int): The level number
        levelName (str): The name of the level
        lives (int): The number of lives
        score (int): The score
        window (pygame.display): The window
    """    
    print("finishWindow")

def pauseMenu(gameLoop, windowWidth, windowHeight, window):
    """The pause menu
    Args:
        gameLoop (Boolean): The game loop
        windowWidth (int): The width of the window
        windowHeight (int): The height of the window
        window (pygame.display): The window
    Returns:
        gameLoop (bool): The game loop
    """
    # Draw background
    background = pygame.image.load("./Game/Assets/Textures/pause_background.png")
    window.blit(background, (0, 0))
    pygame.display.update()
    
    # Write text on the screen
    textFile.writeText(windowWidth*0.5, windowHeight*0.1, "Arial", round(windowWidth*0.05), (0, 0, 0), "Jeu en pause", True, window)
    textFile.writeText(windowWidth*0.5, windowHeight*0.4, "Arial", round(windowWidth*0.03), (0, 0, 0), "Appuyez sur 'Espace' pour continuer ou 'Echap' pour quitter", True, window)
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pause = False
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()

    gameLoop = not pause
    return gameLoop

