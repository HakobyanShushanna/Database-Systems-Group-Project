def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  
            shift_base = 65 if char.isupper() else 97  
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  
    return encrypted_text


def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char 
    return decrypted_text

# if __name__ == "__main__":
#     plain_text = "Hello, World!"
#     shift = 3  # Shift by 3 positions
#
#     encrypted_text = encrypt(plain_text, shift)
#     print(f"Encrypted: {encrypted_text}")
#
#     decrypted_text = decrypt(encrypted_text, shift)
#     print(f"Decrypted: {decrypted_text}")