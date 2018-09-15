import pygame


class Alien(pygame.sprite.Sprite):
    """Represents a single alien in the fleet"""
    def __init__(self, ai_settings, screen):
        """Initialize alien and set starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load alien image and set rect attribute
        self.image = pygame.image.load('images/alien3_resized.png')
        self.death_index = None
        self.last_frame = None
        self.death_frames = []
        self.death_frames.append(pygame.image.load('images/alien_death/alien_green_death1_resized.png'))
        self.death_frames.append(pygame.image.load('images/alien_death/alien_green_death1_resized.png'))
        self.death_frames.append(pygame.image.load('images/alien_death/alien_green_death1_resized.png'))
        self.death_frames.append(pygame.image.load('images/alien_death/alien_green_death1_resized.png'))
        self.rect = self.image.get_rect()
        # Start new aliens at top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store alien's exact position
        self.x = float(self.rect.x)
        # Killed flag
        self.dead = False

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False

    def begin_death(self):
        """Set alien's death flag and begin death animation"""
        self.dead = True
        self.death_index = 0
        self.image = self.death_frames[self.death_index]
        self.last_frame = pygame.time.get_ticks()

    def update(self):
        """Move alien to the right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        if self.dead:
            time_test = pygame.time.get_ticks()
            if abs(self.last_frame - time_test) > 20:   # At least 20 millisecond delay between frames
                self.last_frame = time_test     # Delay should ensure animation is perceivable at high fps
                self.death_index += 1
                if self.death_index >= len(self.death_frames):
                    self.kill()
                else:
                    self.image = self.death_frames[self.death_index]

    def blitme(self):
        """Draw alien at its current location"""
        self.screen.blit(self.image, self.rect)
