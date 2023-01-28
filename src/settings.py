"""Keeping game settings organized in a class."""
from pydantic import BaseModel


class Settings(BaseModel):
    """A class to store all settings for Alien Invasion."""

    screen_width: int = 1200
    screen_height: int = 800
    background_color: tuple = (230, 230, 230)
