"""Module for game internals."""
import sys

import pygame

from src.alien import Alien
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
    elif event.key == pygame.K_q:
        sys.exit()


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


def get_number_rows(game_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen.

    Args:
        game_settings: configurable game settings
        ship_height: height of ship
        alien_height: height of alien

    Returns:
        number of rows of aliens

    """
    available_space_y = (
        game_settings.screen_height - (3 * alien_height) - ship_height
    )
    return int(available_space_y / (2 * alien_height))


def get_number_aliens_x(game_settings, alien_width):
    """Determine the number of aliens that fit in a row.

    Args:
        game_settings: configurable game settings
        alien_width: int specifying alien width

    Returns:
        an int specifying number of aliens

    """
    available_space_x = game_settings.screen_width - 2 * alien_width
    return int(available_space_x / (2 * alien_width))


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row.

    Args:
        game_settings: configurable game settings
        screen: a pygame screen
        aliens: a pygame group of Alien
        alien_number: alien number in fleet
        row_number: number of alien row

    """
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (
        alien.rect.height + 2 * alien.rect.height * row_number  # noqa: WPS221
    )
    aliens.add(alien)


def create_fleet(game_settings, screen, ship, aliens):
    """Create a fleet full of aliens.

    Args:
        game_settings: configurable game settings
        screen: a pygame screen
        aliens: a pygame group of aliens
        ship: a ship object that will move
    """
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(
        game_settings, ship.rect.height, alien.rect.height,
    )

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(
                game_settings,
                screen,
                aliens,
                alien_number,
                row_number,
            )


def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets.

    Args:
        bullets: a pygame group of bullets.
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_aliens(game_settings, aliens):
    """Update position of aliens.

    Args:
        aliens: a pygame group of aliens.
        game_settings: a class containing settings for game
    """
    check_fleet_edges(game_settings, aliens)
    aliens.update()


def update_screen(
    game_settings: Settings,
    screen,
    ship: Ship,
    aliens,
    bullets,
) -> None:
    """Update images and flip to new screen.

    Args:
        game_settings: a class containing settings for game
        screen: a pygame display object that will produce the screen
        ship: a ship object that will move
        bullets: a pygame group of Bullet class
        aliens: a group of aliens
    """
    screen.fill(game_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def check_fleet_edges(game_settings, aliens):
    """Respond appropriately if any aliens have reached an edge.

    Args:
        game_settings: a class containing settings for game
        aliens: a group of aliens
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)


def change_fleet_direction(game_settings, aliens):
    """Drop the entire fleet and change the fleet's direction.

    Args:
        game_settings: a class containing settings for game
        aliens: a group of aliens
    """
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1
