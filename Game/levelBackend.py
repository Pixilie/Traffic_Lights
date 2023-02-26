import pygame


def levelCompleted(carsPassed, carsToPass, level, levelName, levelDescription, lives, score, window):
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
    # FIXME: Never updated -> conditions not met
    print("carsPassed: " + str(carsPassed))
    print("carsToPass: " + str(carsToPass))
    if carsPassed == carsToPass:
        pygame.quit()
