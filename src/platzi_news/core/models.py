"""Data models for Platzi News."""

from dataclasses import dataclass


@dataclass
class Article:
    """Represents a news article."""

    title: str
    description: str
    url: str

    """lorem ipsum lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum"""
