from PIL import Image

def swap_pixels(image):
    width, height = image.size
    pixels = image.load()

    for i in range(width):
        for j in range(height):
            # Swap RGB values
            r, g, b = pixels[i, j]
            pixels[i, j] = (b, r, g)

def apply_math_operation(image, key):
    width, height = image.size
    pixels = image.load()

    for i in range(width):
        for j in range(height):
            # Apply a basic mathematical operation (XOR) to each pixel component
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)

def encrypt_image(image_path, method, key):
    image = Image.open(image_path)

    if method == "swap":
        swap_pixels(image)
    elif method == "math":
        apply_math_operation(image, key)
    else:
        raise ValueError("Invalid encryption method")

    encrypted_path = f"encrypted_{method}_key{key}.png"
    image.save(encrypted_path)
    print(f"Image encrypted using {method} method. Encrypted image saved as {encrypted_path}")

def decrypt_image(encrypted_path, method, key):
    encrypted_image = Image.open(encrypted_path)

    if method == "swap":
        swap_pixels(encrypted_image)
    elif method == "math":
        apply_math_operation(encrypted_image, key)
    else:
        raise ValueError("Invalid encryption method")

    decrypted_path = f"decrypted_{method}_key{key}.png"
    encrypted_image.save(decrypted_path)
    print(f"Image decrypted using {method} method. Decrypted image saved as {decrypted_path}")

def main():
    image_path = input("Enter the path to the image file: ")
    method = input("Choose encryption method ('swap' or 'math'): ")
    key = int(input("Enter the encryption key: "))

    # Encrypt the image
    encrypt_image(image_path, method, key)

    # Decrypt the image
    encrypted_path = f"encrypted_{method}_key{key}.png"
    decrypt_image(encrypted_path, method, key)

if __name__ == "__main__":
    main()
