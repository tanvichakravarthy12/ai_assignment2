import random
import string
import time
from captcha.image import ImageCaptcha
from PIL import Image


def generate_image_captcha(length=5):
    """Generates an image-based CAPTCHA using the `captcha` library."""
    image = ImageCaptcha(width=280, height=90)

    # Generate random characters
    characters = string.ascii_uppercase + string.digits
    captcha_text = ''.join(random.choice(characters) for _ in range(length))

    # Generate the image
    data = image.generate(captcha_text)

    # Save the image temporarily to show to the user
    image_file = "current_captcha.png"
    image.write(captcha_text, image_file)

    return captcha_text, image_file


def captcha_test():
    print("===============================================")
    print("        CAPTCHA Verification System            ")
    print("===============================================")

    attempts_allowed = 3
    attempts = 0
    verified = False

    while attempts < attempts_allowed and not verified:
        expected_answer, image_path = generate_image_captcha()

        print(f"\nChallenge {attempts + 1}/{attempts_allowed}:")
        print("An image CAPTCHA has been generated and opened. Please view it.")

        # Open the image using the default image viewer
        try:
            img = Image.open(image_path)
            img.show()
        except Exception as e:
            print(f"Could not open image automatically: {e}")
            print(f"Please manually open the file '{image_path}' in the current directory.")

        user_input = input(">> Type the text seen in the image: ").strip()

        if user_input.upper() == expected_answer.upper():
            print("\n[SUCCESS] CAPTCHA Passed! You are verified as human.")
            verified = True
        else:
            print("\n[FAILED] Incorrect CAPTCHA.")
            attempts += 1
            if attempts < attempts_allowed:
                print("Please try again.")
                time.sleep(1)  # Slight penalty delay

    if not verified:
        print("\n[ERROR] Verification failed. Maximum attempts reached. Access denied.")
        return False

    return True


if __name__ == "__main__":
    captcha_test()