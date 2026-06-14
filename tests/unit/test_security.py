from app.core.security import (
    hash_password,
    verify_password,
)


def test_hash_password_changes_value():
    password = "secret123"

    hashed = hash_password(password)

    assert hashed != password


def test_verify_password_success():
    password = "secret123"

    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_verify_password_failure():
    password = "secret123"

    hashed = hash_password(password)

    assert verify_password("wrong-password", hashed) is False