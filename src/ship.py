"""Ship class."""
import pygame


class Ship():  # noqa: WPS306
    """Initialize the ship and set its starting position."""

    def __init__(self, game_settings, screen):
        """Ship constructor.

        Args:
            game_settings: a class of game settings
            screen: a pygame screen object.
        """
        self.game_settings = game_settings
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += 1
        if self.moving_left and self.rect.left > 0:
            self.center -= 1
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
