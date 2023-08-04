import cv2
import numpy as np


def check_image(_image: np.ndarray) -> bool:
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


def capture_image(path: str) -> np.ndarray:
    """
    capture image from video
    :param path: absolute path of video
    :return: bgr image numpy array
    """
    try:
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            raise Exception('Failed to open video capture.')

        cap.release()
    except Exception as e:
        # 处理异常情况
        print('An error occurred:', str(e))
        return None

    frames_num = int(cap.get(7))

    temp_img: np.ndarray = None
    check_frames: list[int] = []

    # 如果视频帧数小于24，直接返回第1帧
    if frames_num < 24:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
        _, _image = cap.read()
        return _image

    # 如果视频帧数小于100，只检测5、10、15帧; 如果视频帧数大于100，跳跃检测，最多10次
    if frames_num < 100:
        check_frames = [5, 10, 15]
    else:
        # 生成20以内的随机int数
        for _ in range(10):
            check_frames.append(np.random.randint(0, 10))

    for i in check_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        _, _image = cap.read()
        if i == check_frames[0]:
            temp_img = _image
        if check_image(_image):
            return _image
    return temp_img


if __name__ == '__main__':
    check_image(None)
