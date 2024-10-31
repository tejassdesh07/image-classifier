# QR Code Image Sorter

This project detects Qr code: one for images containing QR codes. It uses Python with the `cv2` library for image handling and `pyzbar` to detect QR codes.

## Features
- Detects QR codes in images and separates them from normal photos.
- Moves images with QR codes to `qr_code_images` folder.
- Easily customizable paths for the data folder and output folders.

## Prerequisites
1. Python 3.6+
2. Install dependencies from `requirements.txt`.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/tejassdesh07/image-classifier.git
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```



## Usage

Place the images to be processed in the `data` folder. Then run the script:

```bash
python index.py
