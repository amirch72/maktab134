def hi_user(name: str) -> str | None:
    if name != "ali":
        return f"Hello {name}"


def bye_user(name: str) -> str:
    return f"Bye {name}"


def test_hi_user():
    assert hi_user("amir") == "Hello amir"


def test_hi_user2():
    assert hi_user("ali") == None


def test_bye_user():
    assert bye_user("amir") == "Bye amir"


# unittest
# self.assertEqual
# self.assertTrue


class User:
    def __init__(self, name):
        self.name = name


def test_user():
    ins_user = User("amir")
    assert ins_user.name == "amir"
