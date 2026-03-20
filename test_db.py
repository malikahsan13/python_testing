from db import Database
import pytest


@pytest.fixture
def db():
    """Provides a fresh instance of the Database class and cleans up after the test"""
    database = Database()
    yield database  # Provides the fixture instance
    database.data.clear()
