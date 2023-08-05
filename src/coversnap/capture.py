import cv2
import numpy as np
from typing import List, Optional


def check_image(_image: Optional[np.ndarray]) -> bool:
    """
    check if the image is valid
    :param _image: bgr image numpy array
    :return: True if the image gray mean value is between 10 and 245
    """
    if _image is None:
        return False
    # 转换为灰度图
    gray_image = cv2.cvtColor(_image, cv2.COLOR_BGR2GRAY)
    # 计算灰度图的颜色均值
    mean_value = cv2.mean(gray_image)[0]
    # 判断颜色均值是否在有效范围内
    return True if 10 < mean_value < 245 else False


def capture_image(path: str) -> Optional[np.ndarray]:
    """
    capture image from video
    :param path: absolute path of video
    :return: bgr image numpy array
    """
    try:
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            cap.release()
            raise Exception('Failed to open video capture.')

    except Exception as e:
        # 处理异常情况
        print('An error occurred:', str(e))
        return None

    frames_num = int(cap.get(7))

    check_frames: List[int] = []

    # 如果视频帧数小于24，直接返回第1帧
    if frames_num < 24:
        check_frames = [1]
    # 如果视频帧数小于100，测试第5、10、15帧
    elif frames_num < 100:
        check_frames = [5, 10, 15]
    else:
        # 生成10以内的随机int数
        for _ in range(10):
            check_frames.append(np.random.randint(0, 10))

    for i in check_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        _, _image = cap.read()
        if check_image(_image):
            cap.release()
            return _image

    cap.release()
    return None
