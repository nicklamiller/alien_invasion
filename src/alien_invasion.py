"""Main module for running Alien Invasion."""
import sys

import pygame

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(game_settings.background_color)
        ship.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    run_game()
