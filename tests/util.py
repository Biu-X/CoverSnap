import cv2
import numpy as np
from pathlib import Path
from typing import List


projectPATH = Path(__file__).resolve().parent.parent.absolute()


def load_image() -> np.ndarray:
    """
    Load an image from the assets folder
    :return:
    """
    test_img: str = str(projectPATH / 'assets' / 'test_pic.jpg')
    img = cv2.imdecode(np.fromfile(test_img, dtype=np.uint8), cv2.IMREAD_COLOR)
    return img


def get_video_path() -> List[str]:
    """
    Get the absolute path of the test video
    [0]: test_video.mp4
    [1]: test_video_1s.mp4
    [2]: test_video_3s.mp4
    [3]: test_video_white.mp4
    [4]: test_video_black.mp4
    :return:
    """
    return [
        str(projectPATH / 'assets' / 'test_video.mp4'),
        str(projectPATH / 'assets' / 'test_video_1s.mp4'),
        str(projectPATH / 'assets' / 'test_video_3s.mp4'),
        str(projectPATH / 'assets' / 'test_video_white.mp4'),
        str(projectPATH / 'assets' / 'test_video_black.mp4')
    ]
