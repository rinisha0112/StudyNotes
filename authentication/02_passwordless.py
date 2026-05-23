# passwordless authentication mechanism works on "something you have" principle. 
# In most cases the something you have becomes your device
# You will get a an OTP on sms or call 
# or on your email
# or a magic link on the email 
# another wonderful way is TOTP 
# which is Time based one-time-password
# this is how microsoft authenticator/ goofle authenticator work. You will be shown a an otp on your authenticator app which is valid for 30/60s
# if you type the same digits on your login page - the server recalculates the digits and verifies.
# the alorithm is based on current time + secret + hmac-sha-1 for authentication
# Base32 encoding is a binary-to-text method that translates raw binary data into a standard, case-insensitive 
# set of 32 readable ASCII characters (A-Z and 2-7). It is primarily used to transmit binary data safely through text-based systems without corruption, while remaining easy for humans to read and type.



from secrets import token_bytes
import base64
import qrcode
import os


# account creation - one time step 
secret = token_bytes(16)
encoded_secret = base64.b32encode(secret)
img = qrcode.make(secret)
image_file_path = os.path.join(os.getcwd(), 'data/authentication/02_passwordless/qr_image.png')
img.save(image_file_path)
