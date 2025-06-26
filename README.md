# PRODIGY_CS_02
🖼️ Task 2: Image Encryption & Decryption Tool
🔧 Description
A basic image encryption tool that uses pixel value manipulation (XOR) to scramble an image, and then reverses the operation to decrypt it.

📜 How It Works
Uses Pillow (PIL) to load the image.

Each pixel's RGB values are XOR-ed with a fixed key (e.g., 123).

The same operation is applied again to decrypt due to XOR's reversible nature.

🖥️ Sample Output
Encrypted image saved as: encrypted.png
Decrypted image saved as: decrypted.png

💡 What You Learn
Skill	Description
Image Processing	Work with pixel data using Pillow
Bitwise Operations	Understand XOR logic for cryptography
File Handling	Open/save images in Python

🛠️ Installation
pip install pillow
▶️ How to Run
python image_encryptor.py
Ensure the input image exists at the path you specify.

