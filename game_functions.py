import sys
import pygame

from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """Handle key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Handle key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Handle key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if the limit has not been reached already"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Update the positions of all bullets, remove bullets that are no longer visible"""
    bullets.update()
    # Remove bullets that are out of view
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, alien, bullets):
    """Update images on the screen and flip to new screen"""
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    pygame.display.flip()
