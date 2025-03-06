from PIL import Image

def get_image_resolution(image_path):
    with Image.open(image_path) as img:
        return img.size

# Example usage
print(get_image_resolution("example.jpg"))