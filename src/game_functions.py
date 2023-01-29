"""Module for game internals."""
import sys

import pygame

from src.settings import Settings
from src.ship import Ship


def check_events(ship: Ship) -> None:
    """Respond to key presses and mouse events.

    Args:
        ship: a Ship object
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(
    event,
    ship: Ship,
) -> None:
    """Respond to key presses.

    Args:
        event: a pygame event
        ship: a Ship object
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True


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


def update_screen(
    game_settings: Settings,
    screen,
    ship: Ship,
) -> None:
    """Update images and flip to new screen.

    Args:
        game_settings: a class containing settings for game
        screen: a pygame display object that will produce the screen
        ship: a ship object that will move
    """
    screen.fill(game_settings.background_color)
    ship.blitme()
    pygame.display.flip()
