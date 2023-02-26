import pygame

def levelCompleted(carsPassed, carsToPass, level, levelName, levelDescription, lives, score, window):
    print(carsPassed) # FIXME: Never updated -> conditions not met
    print(carsToPass)
    if carsPassed == carsToPass:
        pygame.quit()