def caesar_cipher_encrypt(text, shift):
    """
    Encrypts a message using the Caesar Cipher technique.

    Args:
        text (str): The message to be encrypted.
        shift (int): The number of positions to shift each letter.

    Returns:
        str: The encrypted message.
    """
    result = ""

    # Iterate over the given text
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            start = ord('a') if char.islower() else ord('A')
            # Calculate the shifted character
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # If not an alphabet, keep it as is (e.g., spaces, numbers, punctuation)
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    """
    Decrypts a message encrypted with the Caesar Cipher technique.
    This is essentially encrypting with a negative shift.

    Args:
        text (str): The message to be decrypted.
        shift (int): The same shift value used for encryption.

    Returns:
        str: The decrypted message.
    """
    return caesar_cipher_encrypt(text, -shift)

if __name__ == "__main__":
    message = input("Enter the message to encrypt: ")
    try:
        shift_value = int(input("Enter the shift value (an integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        exit()

    encrypted_message = caesar_cipher_encrypt(message, shift_value)
    print(f"\nOriginal Message: {message}")
    print(f"Shift Value: {shift_value}")
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift_value)
    print(f"Decrypted Message: {decrypted_message}")

    # Example with different cases and non-alphabetic characters
    print("\n--- Another Example ---")
    message2 = "Hello, World! 123"
    shift_value2 = 3
    encrypted_message2 = caesar_cipher_encrypt(message2, shift_value2)
    print(f"Original Message: {message2}")
    print(f"Encrypted Message: {encrypted_message2}")
    print(f"Decrypted Message: {caesar_cipher_decrypt(encrypted_message2, shift_value2)}")