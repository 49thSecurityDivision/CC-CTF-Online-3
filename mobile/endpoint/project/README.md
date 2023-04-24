## Leaky Endpoint

## Description
Reverse the application and get the secret from the api service

## Flag
flag{swiper_no_cipher}

## Solution
- Analyze the Flutter mobile app to identify the API key used in the request header.
- Reverse engineer the Python service to understand the Vigenère cipher implementation and find the encryption key.
- Retrieve the encrypted secret message using the Flutter app.
- Decrypt the secret message using the Vigenère cipher implementation discovered in step 2.
