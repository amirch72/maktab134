# import sys, os

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from course_27.course_1404_07_24 import hello, show_name, cal_value


def test_hello():
    assert hello("ramin") == "hello ramin"
    assert hello("amin") == "hello ramin"


def test_hello_3():
    assert hello("niloofar") == "hello niloofar"


def test_hello_2():
    assert hello("amin") == "hello amin"


def test_hello_4():
    assert hello("Ariyan") == "hello Ariyan"


def test_show_name_1():
    assert show_name() == "Zahra Abbasi"


def test_cal_val():
    assert cal_value(1000) == 100
