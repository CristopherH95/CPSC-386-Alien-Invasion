import pygame

import game_functions as gf

from settings import Settings
from ship import Ship
from alien import Alien


# TODO: Continue from pg. 269
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings, screen)
    bullets = pygame.sprite.Group()
    alien = Alien(ai_settings, screen)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


if __name__ == '__main__':
    run_game()
