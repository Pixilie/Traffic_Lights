# Imports
import pygame
import random
import os
import json

# Changing working directory
os.chdir('../Traffic_Lights')
    
def playSound(type, volume, sound):
    """Play a sound.
    Args:
        type (str): Type of sound to play.
        volume (int): Volume of the music.
    """
    pygame.mixer.init()
    soundChannel = pygame.mixer.Channel(3)
    musicChannel = pygame.mixer.Channel(2)
    if type == 'music':
        musicNumber = random.randint(1, 3)
        if musicNumber == 1:
            music = pygame.mixer.Sound('./Game/Assets/Sounds/music1.mp3')
            pygame.mixer.Channel(2).play(music, loops=-1)
        elif musicNumber == 2:
            music = pygame.mixer.Sound('./Game/Assets/Sounds/music2.mp3')
            pygame.mixer.Channel(2).play(music)
        else:
            music = pygame.mixer.Sound('./Game/Assets/Sounds/music3.mp3')
            pygame.mixer.Channel(2).play(music, loops=-1)
    else:
        soundToPlay = pygame.mixer.Sound(sound)
        pygame.mixer.Channel(3).play(soundToPlay)

    soundChannel.set_volume(volume*1.8)
    musicChannel.set_volume(volume*0.7)

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