from coversnap import check_image
from tests.util import load_image


class Test_CHECKIMAGE:
    def test_valid(self):
        assert check_image(load_image()) is True

    def test_none(self):
        assert check_image(None) is False
