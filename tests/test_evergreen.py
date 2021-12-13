import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    # def test_two(self):
    #     x = {"check": True}
    #     assert hasattr(x, "check")


def test_answer():
    assert 1 == 1


def disabled_test_fail():
    assert 1 == 2
