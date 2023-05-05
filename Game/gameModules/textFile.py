import pygame
import json

def writeText(x, y, fontName, fontSize, color, message, center, window):
    """Writes text on the screen
    Args:
        x (int): x position on the screen
        y (int): y position on the screen
        font (string): The font
        size (int): The size of the text
        color (tuple): The color of the text
        message (string): The message to write
        center (bool): If the text is centered or not
        window (pygame.display): The window
    Returns:
        text (sprite): The text
    """    
    pygame.font.init()
    font = pygame.font.SysFont(fontName, fontSize)
    text = font.render(message, True, color)
    width = text.get_rect().width
    if center:
        window.blit(text, (x-width/2, y))
    else:
        window.blit(text, (x, y))
    pygame.display.update()
    return text

def writeData(newData, jsonFile):
    """Writes data in a json file
    Args:
        newData (dict): The data to write
        jsonFile (string): The json file
    """    
    with open(jsonFile, "r+") as f:
        fileData = json.load(f)
        fileData["levels"].append(newData)
        f.seek(0)
        json.dump(fileData, f, indent=4)

def modifyData(levelID, dataToChange, value, jsonFile):
    """Modifies data in a json file
    Args:
        levelID (int): Level ID
        dataToChange (string): Data to change
        value (string/int): Value to change in dataToChange
        jsonFile (string): The json file
    """
    with open(jsonFile, "r+") as f:
        fileData = json.load(f)
        for dataGroup in fileData:
            for d in fileData[dataGroup]:
                if d["level_id"] == levelID:
                    d[dataToChange] = value
        f.seek(0)
        json.dump(fileData, f, indent=4)
        f.truncate()
                
def searchData(dataName, data, jsonFile):
    """Searches data in a json file
    Args:
        dataName (string): The name of the data
        data (string): The data to search
        jsonFile (string): The json file
    """   
    with open(jsonFile, "r") as f:
        fileData = json.load(f)
        for dataGroup in fileData:
            for d in fileData[dataGroup]:
                if d[dataName] == data:
                    return True
        return False

def readData(dataToRead, level, jsonFile):
    """Reads data in a json file
    Args:
        dataToRead (string): The data to read
        level (int): The level
        jsonFile (string): The json file
    """   
    with open(jsonFile, "r") as f:
        fileData = json.load(f)
        for dataGroup in fileData:
            for d in fileData[dataGroup]:
                if d["level_id"] == level:
                    return d[dataToRead]
    return None
                
    