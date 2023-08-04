import cv2
import numpy as np
from pathlib import Path


def load_image() -> np.ndarray:
    projectPATH = Path(__file__).resolve().parent.parent.absolute()
    test_img: str = str(projectPATH / 'assets' / 'test_pic.jpg')

    img = cv2.imdecode(np.fromfile(test_img, dtype=np.uint8), cv2.IMREAD_COLOR)
    return img
