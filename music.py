# Imports
import pygame
import random
import os
import json
import subprocess
import time

# Changing working directory
os.chdir('../Traffic_Lights')
    
def playSound(type, volume):
    """Play a sound.
    Args:
        type (str): Type of sound to play.
        volume (int): Volume of the music.
    """
    pygame.mixer.init()
    sound_channel = pygame.mixer.Channel(0)
    music_channel = pygame.mixer.Channel(1)
    if type == 'music':
        musicNumber = random.randint(1, 3)
        if musicNumber == 1:
            sound1 = pygame.mixer.Sound('./Menus/Assets/Sounds/music1.mp3')
            pygame.mixer.Channel(1).play(sound1, loops=-1)
        elif musicNumber == 2:
            sound2 = pygame.mixer.Sound('./Menus/Assets/Sounds/music2.mp3')
            pygame.mixer.Channel(1).play(sound2)
        else:
            sound3 = pygame.mixer.Sound('./Menus/Assets/Sounds/music3.mp3')
            pygame.mixer.Channel(1).play(sound3, loops=-1)
    else:
        sound0 = pygame.mixer.Sound('./Menus/Assets/Sounds/hover.mp3')
        pygame.mixer.Channel(0).play(sound0)
    sound_channel.set_volume(volume)
    music_channel.set_volume(volume)


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
    setting = { "sound_volume": volume, "language": f"{os.environ['LANG'][:2]}"}
    with open('settings.json', 'w') as settingsFile:
        json.dump(setting, settingsFile, indent=4)