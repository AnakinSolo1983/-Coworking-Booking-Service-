from unittest.mock import Mock # import Mock from unittest.mock

from app.repositories.booking_repository import (
    BookingRepository,
) # import BookingRepository from app.repositories.booking_repository


# test repository creation:
def test_repository_creation():

    db = Mock() # create Mock

    repo = BookingRepository(db) # create BookingRepository

    assert repo is not None # assert repo is not None


# test repository has db:
def test_repository_has_db():

    db = Mock() # create Mock

    repo = BookingRepository(db) # create BookingRepository

    assert repo.db == db # assert repo.db == db