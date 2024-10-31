import os
import cv2
from pyzbar.pyzbar import decode
import shutil

# Folder paths
data_folder = './data'  # Path where images are stored
qr_folder = os.path.join('qr_code_images')
normal_folder = os.path.join('normal_photos')

# Create folders if they don't exist
os.makedirs(qr_folder, exist_ok=True)
os.makedirs(normal_folder, exist_ok=True)

def is_qr_code(image_path):
    """Check if the image contains a QR code using both ZBar and OpenCV."""
    # Try ZBar first
    image = cv2.imread(image_path)
    qr_codes = decode(image)
    if any(code.type == "QRCODE" for code in qr_codes):
        return True
    
    # Fallback to OpenCV if ZBar fails
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(gray)
    return bool(data)

def save_image(image_path, destination_folder):
    """Move image to the specified folder."""
    filename = os.path.basename(image_path)
    dest_path = os.path.join(destination_folder, filename)
    shutil.move(image_path, dest_path)

def process_images():
    """Process all images in the data folder."""
    for filename in os.listdir(data_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(data_folder, filename)
            if is_qr_code(image_path):
                save_image(image_path, qr_folder)
                print(f"{filename} contains a QR code. Moved to qr_code folder.")
            

if __name__ == "__main__":
    process_images()
