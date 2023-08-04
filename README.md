# CoverSnap

A convenient Python library for capturing cover image from video.

[![codecov](https://codecov.io/github/Biu-X/CoverSnap/branch/main/graph/badge.svg?token=FYCR8Y4NDI)](https://codecov.io/github/Biu-X/CoverSnap)
[![CI-test](https://github.com/Biu-X/CoverSnap/actions/workflows/CI-test.yml/badge.svg)](https://github.com/Biu-X/CoverSnap/actions/workflows/CI-test.yml)
[![pip-test](https://github.com/Biu-X/CoverSnap/actions/workflows/pip-test.yml/badge.svg)](https://github.com/Biu-X/CoverSnap/actions/workflows/pip-test.yml)
[![Release](https://github.com/Biu-X/CoverSnap/actions/workflows/Release.yml/badge.svg)](https://github.com/Biu-X/CoverSnap/actions/workflows/Release.yml)
[![PyPI version](https://badge.fury.io/py/CoverSnap.svg)](https://badge.fury.io/py/CoverSnap)
![GitHub](https://img.shields.io/github/license/Biu-X/CoverSnap)

## Installation

You can install CoverSnap using pip (python >= 3.8):

```bash
pip install coversnap
```

## CLI

```
usage: coversnap [-h] -i INPUT -o OUTPUT

Capture image from video and save it to file, return black image if failed

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --INPUT INPUT
                        absolute path to input video
  -o OUTPUT, --OUTPUT OUTPUT
                        absolute path to output image
```

## Python

To capture a cover image from a video, use the `capture_image` function provided by the CoverSnap library. Here's an
example of how to use it:

```python
import os
import cv2
from coversnap import capture_image

input_video = "path/to/video.mp4"
output_image = "path/to/output.jpg"

# Capture the cover image from the video
img = capture_image(input_video)

# Save the captured image to the specified file
_, file_extension = os.path.splitext(output_image)
cv2.imencode(file_extension, img)[1].tofile(output_image)
```

## Development

#### Environment Setup

Before getting started with development, make sure you have the following tools and dependencies installed:

- Python 3.8 or higher
- [PDM](https://pdm.fming.dev/) (Python Development Master)

#### Installing Development Dependencies

In the project's root directory, run the following command to install the development dependencies:

```bash
pdm run dev
```

#### Running Tests

```bash
pdm run test
```

This will run the tests and generate test coverage reports. The test results will be displayed in the terminal, and XML
and HTML format coverage reports will also be generated.

#### Code Style Checking and Static Type Checking

```bash
pdm run lint
```

This will run the code style checking and static type checking. The results will be displayed in the terminal.

## License

CoverSnap is licensed under the MIT License.
