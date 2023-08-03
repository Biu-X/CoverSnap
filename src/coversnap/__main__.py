import cv2

from coversnap.hello import sayhi


def main():
    print('Hello, world!')


if __name__ == '__main__':
    main()
    sayhi()
    print(cv2.haveOpenVX())
