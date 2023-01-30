"""Define bullet class."""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from ship."""

    def __init__(self, game_settings, screen, ship):
        """Create bullet object at ship's current position.

        Args:
            game_settings: a class with game settings
            screen: a pygame screen
            ship: a ship object
        """
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(
            0,
            0,
            game_settings.bullet_width,
            game_settings.bullet_height,
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y_position = float(self.rect.y)
        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """Move bullet up the screen."""
        self.y_position -= self.speed_factor
        self.rect.y = self.y_position

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
