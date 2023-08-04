import argparse
import os
import cv2
import numpy as np
from coversnap import capture_image


def main() -> None:
    # parse args
    parser = argparse.ArgumentParser()
    parser.description = 'Capture image from video and save it to file, return black image if failed'
    parser.add_argument(
        '-i', '--INPUT', help='absolute path to input video', type=str, required=True)
    parser.add_argument(
        '-o', '--OUTPUT', help='absolute path to output image', type=str, required=True)
    args = parser.parse_args()

    _, file_extension = os.path.splitext(args.OUTPUT)
    file_extension = file_extension.lower()
    if file_extension not in ['.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.gif',
                              '.pbm', '.pgm', '.ppm', '.webp', '.hdr', '.pfm', '.exr']:
        print(f'Maybe unsupported file extension: {file_extension}')

    img = capture_image(args.INPUT)

    if img is None:
        print('Failed to capture image, using black image instead')
        img = np.zeros((512, 512, 3), dtype=np.uint8)

    cv2.imencode(file_extension, img)[1].tofile(args.OUTPUT)
    print(f'Cover saved to {args.OUTPUT}')


if __name__ == '__main__':
    main()
