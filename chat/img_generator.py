from PIL import Image
import base64
from io import BytesIO

def generate_image():
    img = Image.new('RGB', (200, 200), color = 'red')
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return img_str