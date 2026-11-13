from app.user_manager import UserManager


def test_add_user():
    manager = UserManager()
    result = manager.add_user("Hiba")

    assert result is True
    assert "Hiba" in manager.get_users()


def test_add_duplicate_user():
    manager = UserManager()
    manager.add_user("Hiba")

    result = manager.add_user("Hiba")

    assert result is False


def test_delete_user():
    manager = UserManager()
    manager.add_user("Hiba")

    result = manager.delete_user("Hiba")

    assert result is True
    assert "Hiba" not in manager.get_users()