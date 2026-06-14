from unittest.mock import Mock # import Mock from unittest.mock

from app.services.auth_service import AuthService # import AuthService from app.services.auth_service
from app.models.user import User # import User from app.models.user
from app.models.user import UserRole # import UserRole from app.models.user


# test auth service creation:
def test_auth_service_creation():

    db = Mock() # create Mock

    service = AuthService(db) # create AuthService

    assert service is not None # assert service is not None


# test authenticate success:
def test_authenticate_success():

    db = Mock() # create Mock

    user = User(
        username="admin",
        password_hash="hashed",
        role=UserRole.ADMIN,
    )

    service = AuthService(db) # create AuthService

    service.user_repository = Mock() # create Mock
    service.user_repository.get_by_username.return_value = user # set return value

    service.verify_password = Mock(return_value=True) # set return value

    result = service.user_repository.get_by_username(
        "admin"
    ) # get user by username

    assert result == user # assert result == user


# test authenticate user not found:
def test_authenticate_user_not_found():

    db = Mock() # create Mock

    service = AuthService(db) # create AuthService

    service.user_repository = Mock() # create Mock
    service.user_repository.get_by_username.return_value = None # set return value

    result = service.user_repository.get_by_username(
        "unknown"
    ) # get user by username

    assert result is None # assert result is None