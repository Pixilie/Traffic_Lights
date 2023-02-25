# Level Information
level = 1 # Level number
levelName = "Niveau 1" # Level name
levelDescription = "Le premier niveau est un niveau d'initiation. Il vous permettra de vous familiariser avec le jeu. Vous devrez apprendre à gérer les feux de signalisation et à éviter les collisions. Bonne chance !" # Level description
completed = False # If the level is completed
lives = 3 # Number of lives
score = 0 # Score of the player
carsToPass = 10 # How many cars the player has to pass to complete the level

# Changing path and import game files
import map
import carFile
import trafficLightFile

# Pygame init
import pygame
from pygame.locals import *
pygame.init()

# Variables
screenWidth = pygame.display.Info().current_w
screenHeight = pygame.display.Info().current_h
white = (255, 255, 255)
clock = pygame.time.Clock()

# Main window setup
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(f'Traffic Light - {levelName}')
window.fill(white)

# Sprites list
spritesList, roadList, trafficLightsList = map.loadMap("./Game/Assets/Maps/map_lvl1.txt", window)
redTrafficLightsList = pygame.sprite.Group()
carList = pygame.sprite.Group()

# Create the cars (will be changed later, just for testing)
car = carFile.car(20, 30, 2, 1)
car2 = carFile.car(5, 30, 2, 2)
spritesList.add(car)
spritesList.add(car2)
carList.add(car)
carList.add(car2)

# Event loop
gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameLoop = False
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            for trafficLight in trafficLightsList:
                trafficLightFile.trafficLightsUpdate(trafficLight, x, y) # Update the traffic lights #FIXME: crash quand on clique sur l'écran

    for car in carList:    
        carList, spritesList = carFile.collisionCars(car, carList, spritesList) # Check if the cars collide with each other
        # car.speed = carFile.collisionRedLights(car, trafficLightsList) # Check if the cars collide with the red lights
        carList, spritesList = carFile.update(car, spritesList, carList) # Update the cars
                
    map.loadMap("./Game/Assets/Maps/map_lvl1.txt", window) # Load the map
    window.fill(white) # Fill the window with white
    spritesList.draw(window) # Draw the sprites
    pygame.display.flip() # Update the display
    displayRate = clock.tick(60) # Limit the display rate to 60 fps
pygame.quit()
