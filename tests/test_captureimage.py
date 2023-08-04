from tests.util import get_video_path
from coversnap import capture_image, check_image


class Test_CHECKCAPTURE:
    def test_none(self) -> None:
        assert capture_image('') is None

    def test_video(self) -> None:
        assert check_image(capture_image(get_video_path()[0]))

    def test_video_1s(self) -> None:
        assert check_image(capture_image(get_video_path()[1]))

    def test_video_3s(self) -> None:
        assert check_image(capture_image(get_video_path()[2]))

    def test_video_white(self) -> None:
        assert capture_image(get_video_path()[3]) is None

    def test_video_black(self) -> None:
        assert capture_image(get_video_path()[4]) is None
