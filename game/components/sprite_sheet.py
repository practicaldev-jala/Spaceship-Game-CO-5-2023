import pygame

class SpriteSheet:
    def __init__(self, sheet):
        self.sheet = sheet
    
    def get_from_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame[0] * width), (frame[1] * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image