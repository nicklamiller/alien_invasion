"""Main module for running Alien Invasion."""
import pygame
from pygame.sprite import Group

import src.game_functions as gf  # noqa: WPS301
from src.settings import Settings
from src.ship import Ship


def run_game():  # noqa: WPS213
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (
            game_settings.screen_width,
            game_settings.screen_height,
        ),
    )  # noqa: F841
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(game_settings, screen)
    bullets = Group()

    while True:

        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(game_settings, screen, ship, bullets)
        screen.fill(game_settings.background_color)
        ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    run_game()
