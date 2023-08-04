import argparse
import os
import cv2
from coversnap import capture_image


def main() -> None:
    # parse args
    parser = argparse.ArgumentParser()
    parser.description = ''
    parser.add_argument(
        '-i', '--INPUT', help='absolute path to input video', type=str, required=True)
    parser.add_argument(
        '-o', '--OUTPUT', help='absolute path to output image', type=str, required=True)
    args = parser.parse_args()

    _, file_extension = os.path.splitext(args.OUTPUT)
    file_extension = file_extension.lower()
    if file_extension not in ['.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.gif',
                              '.pbm', '.pgm', '.ppm', '.webp', '.hdr', '.pfm', '.exr']:
        raise ValueError(f'Unsupported file extension: {file_extension}')

    img = capture_image(args.INPUT)

    cv2.imencode(file_extension, img)[1].tofile(args.OUTPUT)


if __name__ == '__main__':
    main()
