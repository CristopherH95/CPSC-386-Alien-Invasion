import pygame
import random


class Star(pygame.sprite.Sprite):
    """Manages sprites for stars to be displayed in the background"""
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.images = []
        self.images.append(pygame.image.load('images/star/star1_new.png'))
        self.images.append(pygame.image.load('images/star/star2_new.png'))
        self.images.append(pygame.image.load('images/star/star3_new.png'))
        self.index = 0
        self.last_update = pygame.time.get_ticks()   # time check prevents animation from going too fast
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.move_ip(random.randint(0, ai_settings.screen_width),
                          random.randint(0, ai_settings.screen_height))

    def update(self):
        """Iterates through images on update to create animation"""
        time_test = pygame.time.get_ticks()
        if abs(self.last_update - time_test) > 500:
            self.last_update = time_test
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
                self.images.reverse()   # The pictures transition in reverse at the end of each full loop
            self.image = self.images[self.index]