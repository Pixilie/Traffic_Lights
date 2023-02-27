import pygame


def isLevelFinished(carsPassed, carsToPass, level, levelName, levelDescription, lives, score, window, gameLoop):
    """
    Checks if the level is completed
    :param carsPassed: The number of cars that passed
    :param carsToPass: The number of cars that need to pass
    :param level: The level number
    :param levelName: The name of the level
    :param levelDescription: The description of the level
    :param lives: The number of lives
    :param score: The score
    :param window: The window
    """
    if carsPassed == carsToPass or lives == 0:
        gameLoop = not gameLoop
        finishWindow(level, levelName, levelDescription, lives, score, window)
    else:
        return gameLoop


# TODO: Faire la fenêtre de fin de niveau
def finishWindow(level, levelName, levelDescription, lives, score, window):
    print("finishWindow")
