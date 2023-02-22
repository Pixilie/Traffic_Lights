# Level Information
level = 1 # Level number
levelName = "Niveau 1" # Level name
levelDescription = "Le premier niveau est un niveau d'initiation. Il vous permettra de vous familiariser avec le jeu. Vous devrez apprendre à gérer les feux de signalisation et à éviter les collisions. Bonne chance !" # Level description
completed = False # If the level is completed
lives = 3 # Number of lives
score = 0 # Score of the player
carsToPass = 10 # How many cars the player has to pass to complete the level

# Changing path and import game files
import loadMap

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

# Event loop
open = True
while open:
    for event in pygame.event.get():
        if event.type == QUIT:
            open = False
    loadMap.loadMap("./Game/Assets/Maps/map_lvl1.txt", window)
    pygame.display.update()
pygame.quit()
