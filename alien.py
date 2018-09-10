import pygame


class Alien(pygame.sprite.Sprite):
    """Represents a single alien in the fleet"""
    def __init__(self, ai_settings, screen):
        """Initialize alien and set starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load alien image and set rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        # Start new aliens at top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at its current location"""
        self.screen.blit(self.image, self.rect)
