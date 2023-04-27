import pygame

def write(x, y, font, size, color, message, center, window):
    """Writes text on the screen
    Args:
        x (int): x position on the screen
        y (int): y position on the screen
        font (string): The font
        size (int): The size of the text
        color (tuple): The color of the text
        message (string): The message to write
        window (pygame.display): The window
    Returns:
        text (sprite): The text
    """    
    pygame.font.init()
    font = pygame.font.SysFont(font, size)
    text = font.render(message, True, color)
    width = text.get_rect().width
    if center:
        window.blit(text, (x-width/2, y))
    else:
        window.blit(text, (x, y))
    pygame.display.update()
    return text