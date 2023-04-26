import pygame
import os

# Changing working directory
os.chdir('../Traffic_Lights')


def isLevelFinished(carsPassed, carsToPass, level, levelName, lives, score, window, gameLoop):
    """Checks if the level is finished
    Args:
        carsPassed (int): The number of cars that passed
        carsToPass (int): The number of cars to pass
        level (int): The level number
        levelName (str): The name of the level
        levelDescription (str): The description of the level
        lives (int): The number of lives
        score (int): The score
        window (pygame.display): The window
        gameLoop (bool): The game loop
    Returns:
        gameLoop (bool): The game loop
    """
    if carsPassed == carsToPass or lives == 0:
        gameLoop = not gameLoop
        finishWindow(level, levelName, levelDescription, lives, score, window)
    else:
        return gameLoop


# TODO: Faire la fenêtre de fin de niveau
def finishWindow(level, levelName, levelDescription, lives, score, window):
    """The window that appears when the level is finished
    Args:
        level (int): The level number
        levelName (str): The name of the level
        levelDescription (str): The description of the level
        lives (int): The number of lives
        score (int): The score
        window (pygame.display): The window
    """    
    print("finishWindow")
