from PIL import Image

def encrypt_image(img_path, output_path):
    img = Image.open(img_path)
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ 123, g ^ 123, b ^ 123)  # XOR-based encryption
    img.save(output_path)

def decrypt_image(img_path, output_path):
    encrypt_image(img_path, output_path)  # Same operation since XOR is reversible

# Example usage
# encrypt_image("input.png", "encrypted.png")
# decrypt_image("encrypted.png", "decrypted.png")
