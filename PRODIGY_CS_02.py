from PIL import Image

XOR_KEY = 123

def encrypt_image(img_path, output_path):
    img = Image.open(img_path).convert("RGB")  # Ensure RGB mode
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ XOR_KEY, g ^ XOR_KEY, b ^ XOR_KEY)

    img.save(output_path)
    print(f"[+] Image encrypted and saved to: {output_path}")

def decrypt_image(img_path, output_path):
    img = Image.open(img_path).convert("RGB")  # Ensure RGB mode
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ XOR_KEY, g ^ XOR_KEY, b ^ XOR_KEY)

    img.save(output_path)
    print(f"[+] Image decrypted and saved to: {output_path}")


# Example Usage:
# Encrypt
#encrypt_image("C:/Users/Ali/Desktop/convert-jpg-to-png.png", "C:/Users/Ali/Desktop/encrypted.png")

# Decrypt 
#decrypt_image("C:/Users/Ali/Desktop/encrypted.png", "C:/Users/Ali/Desktop/decrypted.png")
