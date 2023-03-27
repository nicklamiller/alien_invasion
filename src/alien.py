"""Add aliens to game."""
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position.

        Args:
            ai_settings: game settings
            screen: A pygame surface

        """
        super(Alien, self).__init__()  # noqa: WPS608
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)  # noqa: WPS111

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
