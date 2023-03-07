# Imports
import pygame
import random
import os
import json
import subprocess

# Changing working directory
os.chdir('../Traffic_Lights')

def playMusic(volume):
    """Play music in loop.
    Args:
        volume (float): Volume of the music.
    """
    pygame.mixer.init()
    playlist = list()
    musicNumber = random.randint(1, 3)
    if musicNumber == 1:
        pygame.mixer.music.load('./Menus/Assets/Sounds/music3.mp3')
    elif musicNumber == 2:
        pygame.mixer.music.load('./Menus/Assets/Sounds/music2.mp3')
    else:
        pygame.mixer.music.load('./Menus/Assets/Sounds/music1.mp3')
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()


def playSound(volume):
    """Play a sound.
    Args:
        sound (str): Path to the sound.
    """
    pygame.mixer.init()
    pygame.mixer.music.load("./Menus/Assets/Sounds/hover.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()


def getVolume():
    """Get the volume level.
    Returns:
        volumeLevel (int): Volume of the music.
    """
    settingsFile = open('settings.json')
    settings = json.load(settingsFile)
    for setting in settings:
        if setting == 'sound_volume':
            volumeLevel = settings[setting]
    settingsFile.close()
    return volumeLevel


def setVolume(volume):
    """Set the volume level.

    Args:
        volume (int): Volume of the music.
    """    
    setting = { "sound_volume": volume}
    with open('settings.json', 'w') as settingsFile:
        json.dump(setting, settingsFile, indent=4)