from flask import Flask, render_template, request, redirect, url_for
from compress_and_classify import classify_and_move_image
import os

app = Flask(__name__)

# Configure paths for file uploads and classifications
app.config['UPLOAD_FOLDER'] = 'static/uploads/data'
app.config['QR_CODE_FOLDER'] = 'static/qr_codes'
app.config['NORMAL_PHOTO_FOLDER'] = 'static/normal_photos'

# Ensure that the required directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['QR_CODE_FOLDER'], exist_ok=True)
os.makedirs(app.config['NORMAL_PHOTO_FOLDER'], exist_ok=True)


@app.route('/')
def index():
    """Display the main upload page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_and_process():
    """Handle the file upload and classification."""
    files = request.files.getlist('images')  # Get the list of uploaded files

    for file in files:
        if file.filename != '':  # Only process files that have a filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)  # Save the file temporarily

            # Process the image (classify and move to appropriate folder)
            classify_and_move_image(file_path)  # This should classify and move the image to QR_CODE_FOLDER or NORMAL_PHOTO_FOLDER

    return redirect(url_for('show_results'))  # Redirect to the results page


@app.route('/results')
def show_results():
    """Display the gallery of classified images."""
    # Get the list of images in the QR and normal photo folders
    qr_code_images = [f for f in os.listdir(app.config['QR_CODE_FOLDER']) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'svg'))]
    normal_images = [f for f in os.listdir(app.config['NORMAL_PHOTO_FOLDER']) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'svg'))]
    
    return render_template('gallery.html', qr_code_images=qr_code_images, normal_images=normal_images)


if __name__ == '__main__':
    app.run(debug=True)
