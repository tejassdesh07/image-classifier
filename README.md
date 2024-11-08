
# Image Classifier

A Flask-based web application that allows users to upload images, classify them into QR codes and normal photos, and view classified images in a gallery.

## Prerequisites

- Python 3.7 or higher

## Setup Guide

### 1. Clone or Download the Repository
To download the files to your computer, you can either:
- [Download ZIP](https://github.com/tejassdesh07/image-classifier/archive/refs/heads/main.zip) and extract the repository to your local machine, or
- Clone the repository using Git:
  ```bash
  git clone https://github.com/tejassdesh07/image-classifier.git
  ```

### 2. Set Up the Virtual Environment
Using a virtual environment helps keep dependencies organized and avoids conflicts with other projects.

#### On Windows
1. Open a terminal or Command Prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/image-classifier
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

#### On macOS
1. Open a terminal.
2. Navigate to the project directory:
   ```bash
   cd path/to/image-classifier
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### 3. Install Required Libraries
With the virtual environment activated, install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Place .env File
Place the .env file in the root directory of the project (the same directory where app.py is located). This will ensure that the application can securely access the required keys.

### 5. Run the Application
Start the Flask application:

```bash
python app.py
```

The app will be accessible locally at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Using the App

1. Open the app in your web browser by visiting [http://127.0.0.1:5000](http://127.0.0.1:5000).
2. Use the "Choose Files" button to upload images, then click "Upload."
3. View the classified images in the gallery by accessing separate sections for QR codes and normal photos.

## Directory Structure

- `static/uploads/data`: Temporary storage for uploaded images before classification.
- `static/qr_codes`: Stores classified QR code images.
- `static/normal_photos`: Stores classified normal photos.

### Note:
The `static` folder, along with its subdirectories (`uploads/data`, `qr_codes`, and `normal_photos`), will be automatically created once an image is uploaded for classification. There is no need to manually create these folders.
