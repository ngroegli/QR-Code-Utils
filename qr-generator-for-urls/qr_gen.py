import qrcode
from PIL import Image

def generate_qr(data, output_path):
    qr = qrcode.QRCode(
        version=20,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=50,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="white", back_color="black")
    qr_img.save(output_path)


def main():
    data_to_encode = "https://example.com"
    output_file = "qr.png"

    generate_qr(data_to_encode, output_file)


if __name__ == "__main__":
    main()