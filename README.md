# Image Classifier

This project is an image classifier that identifies whether images contain QR codes or are regular photos. It utilizes the OpenAI API for classification and incorporates image processing techniques for resizing and encoding.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)


## Features
- Resizes images to a maximum of 500x500 pixels.
- Compresses images for efficient processing.
- Encodes images to Base64 format for API submission.
- Classifies images as either containing a QR code or as normal photos.
- Organizes images into separate folders based on classification.

## Requirements
- Python 3.x
- Required libraries are listed in `requirements.txt`:
  - `openai`
  - `Pillow`
  - `python-dotenv`


## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/tejassdesh07/image-classifier.git
   ```
2. Navigate to the project directory:
   ```bash
   cd image-classifier
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```


## Usage
1. Place your images in the `./data/` directory.
2. Run the main script:
   ```bash
   python main.py
   ```
3. The images will be classified and moved to either the `./qr_codes/` or `./normal_photos/` folder based on the classification result.

