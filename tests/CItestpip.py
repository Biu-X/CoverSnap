import os
from pathlib import Path


def GithubAction_PIP_Test() -> None:
    projectPATH = Path(__file__).resolve().parent.parent.absolute()
    input_video = str(projectPATH / 'assets' / 'test_video.mp4')
    output_image = str(projectPATH / 'assets' / 'test_image.jpg')
    os.system('coversnap -i {} -o {}'.format(input_video, output_image))


if __name__ == '__main__':
    GithubAction_PIP_Test()
