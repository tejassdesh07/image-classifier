from openai import OpenAI
import base64
import os
import shutil
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def compress_image(image_path, output_path, max_size=(500, 500)):
    with Image.open(image_path) as img:
        # Convert image to RGB if it's in a mode that cannot be saved as JPEG
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.thumbnail(max_size)
        img.save(output_path, "JPEG", quality=85)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def classify_and_move_image(image_path):
    compressed_image_path = "./compressed_image.jpg"
    compress_image(image_path, compressed_image_path)

    base64_image = encode_image(compressed_image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Does this image contain a QR code? Respond with 'QR code detected' or 'normal photo'.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }]
    )

    result = response.choices[0].message.content
    print(f"Processing {os.path.basename(image_path)}: {result}")

    target_folder = "./static/qr_codes" if "QR code detected" in result else "./static/normal_photos"
    os.makedirs(target_folder, exist_ok=True)
    shutil.move(image_path, os.path.join(target_folder, os.path.basename(image_path)))

image_folder = "./static/uploads/data/"
for filename in os.listdir(image_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        classify_and_move_image(os.path.join(image_folder, filename))
