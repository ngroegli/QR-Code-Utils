import qrcode
from PIL import Image

def generate_qr_with_image(data, image_path, output_path):
    qr = qrcode.QRCode(
        version=20,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=50,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="white", back_color="black")

    # Open and resize the image
    img = Image.open(image_path)
    img = img.resize((1000, 1000))  # Adjust size as needed

    # Calculate position to paste the image at the center of the QR code
    position = ((qr_img.size[0] - img.size[0]) // 2, (qr_img.size[1] - img.size[1]) // 2)

    # Paste the image on the QR code
    qr_img.paste(img, position)
    qr_img.save(output_path)


def main():
    data_to_encode = "https://example.com"
    image_to_embed = "image_to_embed.jpg"
    output_file = "qr.png"

    generate_qr_with_image(data_to_encode, image_to_embed, output_file)


if __name__ == "__main__":
    main()