# Imports
import pygame
import random
import os
import json

# Changing working directory
os.chdir('../Traffic_Lights')
    
def playSound(type, volume):
    """Play a sound.
    Args:
        type (str): Type of sound to play.
        volume (int): Volume of the music.
    """
    pygame.mixer.init()
    soundChannel = pygame.mixer.Channel(0)
    musicChannel = pygame.mixer.Channel(1)
    if type == 'music':
        musicNumber = random.randint(1, 3)
        if musicNumber == 1:
            music = pygame.mixer.Sound('./Menus/Assets/Sounds/music1.mp3')
            pygame.mixer.Channel(1).play(music, loops=-1)
        elif musicNumber == 2:
            music = pygame.mixer.Sound('./Menus/Assets/Sounds/music2.mp3')
            pygame.mixer.Channel(1).play(music)
        else:
            music = pygame.mixer.Sound('./Menus/Assets/Sounds/music3.mp3')
            pygame.mixer.Channel(1).play(music, loops=-1)
    else:
        hoverSound = pygame.mixer.Sound('./Menus/Assets/Sounds/hover.mp3')
        pygame.mixer.Channel(0).play(hoverSound)
    soundChannel.set_volume(volume)
    musicChannel.set_volume(volume)


def getVolume():
    """Get the volume level.
    Returns:
        volumeLevel (int): Volume of the music.
    """
    settingsFile = open('settings.json')
    settings = json.load(settingsFile)
    for setting in settings:
        if setting == 'sound_volume':
            volumeLevel = float(settings[setting])/100
    settingsFile.close()
    return volumeLevel

def setVolume(volume):
    """Set the volume level.
    Args:
        volume (int): Volume of the music.
    """
    setting = { "sound_volume": volume, "language": f""}
    with open('settings.json', 'w') as settingsFile:
        json.dump(setting, settingsFile, indent=4)