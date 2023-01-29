"""Main module for running Alien Invasion."""
import pygame

import game_functions as gf  # type: ignore
from src.settings import Settings
from src.ship import Ship


def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (
            game_settings.screen_width,
            game_settings.screen_height,
        ),
    )  # noqa: F841
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen)

    while True:

        gf.check_events()

        screen.fill(game_settings.background_color)
        ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    run_game()
