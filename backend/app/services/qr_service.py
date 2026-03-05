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
