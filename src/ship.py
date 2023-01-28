"""Ship class."""
import pygame


class Ship():  # noqa: WPS306
    """Initialize the ship and set its starting position."""

    def __init__(self, screen):
        """Ship constructor.

        Args:
            screen: a pygame screen object.
        """
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
