import smtplib
import ssl
from email.message import EmailMessage
from smtp_config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD

RECEIVER_EMAIL = SENDER_EMAIL  # send to yourself first
OTP = "748392"

msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = "OTP Verification Test"
msg.set_content(f"Your OTP is {OTP}. It expires in 5 minutes.")

context = ssl.create_default_context()

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls(context=context)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

    print("[SUCCESS] OTP email sent")

except Exception as e:
    print("[FAILURE]", e)
