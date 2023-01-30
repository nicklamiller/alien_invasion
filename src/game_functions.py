"""Module for game internals."""
import sys

import pygame

from src.bullet import Bullet
from src.settings import Settings
from src.ship import Ship


def check_events(
    game_settings,
    screen,
    ship: Ship,
    bullets,
) -> None:
    """Respond to key presses and mouse events.

    Args:
        game_settings: configurable game settings
        screen: a pygame screen
        ship: a Ship object
        bullets: a pygame group of the Bullet object
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(
                event,
                game_settings,
                screen,
                ship,
                bullets,
            )

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(
    event,
    game_settings,
    screen,
    ship: Ship,
    bullets,
) -> None:
    """Respond to key presses.

    Args:
        event: a pygame event
        game_settings: configurable game settings
        screen: a pygame screen
        ship: a Ship object
        bullets: a pygame group of Bullet class
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(
    event,
    ship: Ship,
) -> None:
    """Respond to key releases.

    Args:
        event: a pygame event
        ship: a Ship object
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(
    game_settings,
    screen,
    ship,
    bullets,
):
    """Fire a bullet if limit not reached yet.

    Args:
        game_settings: configurable game settings
        screen: a pygame screen
        ship: a Ship
        bullets: a pygame group of bullets
    """
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets.

    Args:
        bullets: a pygame group of bullets.
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(
    game_settings: Settings,
    screen,
    ship: Ship,
    bullets,
) -> None:
    """Update images and flip to new screen.

    Args:
        game_settings: a class containing settings for game
        screen: a pygame display object that will produce the screen
        ship: a ship object that will move
        bullets: a pygame group of Bullet class
    """
    screen.fill(game_settings.background_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
