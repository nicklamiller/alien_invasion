"""Keeping game settings organized in a class."""
from pydantic import BaseModel


class Settings(BaseModel):
    """A class to store all settings for Alien Invasion."""

    screen_width: int = 1200
    screen_height: int = 800
    background_color: tuple = (230, 230, 230)
    ship_speed_factor: float = 1.5
    bullet_speed_factor = 1
    bullet_width = 3
    bullet_height = 15
    bullet_color = 60, 60, 60
    bullets_allowed = 3
