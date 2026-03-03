import pyotp
import base64
import io
import qrcode

def generate_mfa_secret():
    return pyotp.random_base32()

def generate_qr_code(username: str, secret: str):
    totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(
        name=username,
        issuer_name="CapstoneBank"
    )

    qr = qrcode.make(totp_uri)
    buffered = io.BytesIO()
    qr.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def verify_mfa_code(secret: str, code: str):
    totp = pyotp.TOTP(secret)
    return totp.verify(code)