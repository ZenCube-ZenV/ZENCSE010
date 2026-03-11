"""
QR Code Generation Service.

TODO (Students):
  Implement one function:

  generate_qr_base64(verification_url: str) -> str
    - Use the `qrcode` library to generate a QR code image
    - The QR code should encode the full verification_url string
      e.g. "http://localhost:3001/v/CERT-550e8400..."
    - Error correction level: ERROR_CORRECT_M
    - Save to a BytesIO buffer as PNG
    - Return the image as a base64-encoded string

  Hint:
    import qrcode, io, base64
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(verification_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()
"""

# TODO: implement QrService here
import qrcode
import io
import base64

def generate_qr_base64(verification_url: str) -> str:
    """
    Generates a PNG QR code from a verification URL and returns it as a base64-encoded string.
    """
    # 1. Initialize the QRCode with ERROR_CORRECT_M error correction
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    
    # 2. Add the verification URL data to the QR code
    qr.add_data(verification_url)
    qr.make(fit=True)
    
    # 3. Create the image as a PNG (black fill, white background)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # 4. Save to a BytesIO buffer as PNG
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    
    # 5. Return the image as a base64-encoded string
    return base64.b64encode(buffer.getvalue()).decode('utf-8')

