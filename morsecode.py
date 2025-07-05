def get_morse_code_map():
    """
    Returns a dictionary mapping characters to their Morse code representations.
    """
    return {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
        '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
        '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
        ' ': '/'  # Space between words is represented by a single slash
    }

def get_reverse_morse_code_map(morse_map):
    """
    Returns a dictionary mapping Morse code representations back to characters.
    """
    return {value: key for key, value in morse_map.items()}

def encrypt_to_morse(message):
    """
    Encrypts a text message into Morse code.

    Args:
        message (str): The message to be encrypted.

    Returns:
        str: The encrypted message in Morse code, with spaces between
             character codes and a single slash for word spaces.
    """
    morse_map = get_morse_code_map()
    encrypted_message = []
    # Convert message to uppercase to match dictionary keys
    message = message.upper()

    for char in message:
        if char in morse_map:
            encrypted_message.append(morse_map[char])
        else:
            # Handle characters not in the map (e.g., unknown symbols)
            # You might choose to ignore them, add a placeholder, or raise an error
            print(f"Warning: Character '{char}' not found in Morse code map. Skipping.")
    # Join character codes with a space, and words with a triple space (standard)
    # The ' ' in the map is handled, so we just join the individual character codes.
    # A single space in the input becomes a '/' in the output, so we need to
    # handle word separation carefully.
    # For simplicity, we'll use ' ' between character codes and '/' for word spaces.
    # If the input has multiple spaces, they will all become '/'.
    return ' '.join(encrypted_message)

def decrypt_from_morse(morse_message):
    """
    Decrypts a Morse code message back into text.

    Args:
        morse_message (str): The Morse code message to be decrypted.
                             Character codes should be separated by spaces,
                             and word spaces by a single slash '/'.

    Returns:
        str: The decrypted text message.
    """
    morse_map = get_morse_code_map()
    reverse_morse_map = get_reverse_morse_code_map(morse_map)
    decrypted_message = []

    # Split the message into individual Morse code units (characters or word spaces)
    # A single space separates character codes, a '/' separates words.
    # We replace '/' with a unique temporary delimiter to split correctly,
    # then split by space, then replace the delimiter back to a space.
    # This handles cases where multiple spaces might be in the input.
    word_separated_codes = morse_message.split(' / ') # Split by word separator

    for word_codes in word_separated_codes:
        char_codes = word_codes.split(' ') # Split each word into character codes
        for code in char_codes:
            if code in reverse_morse_map:
                decrypted_message.append(reverse_morse_map[code])
            else:
                # Handle unknown Morse codes
                print(f"Warning: Morse code '{code}' not found in map. Skipping.")
        decrypted_message.append(' ') # Add space between words
    
    # Remove the trailing space if any
    return "".join(decrypted_message).strip()

if __name__== "__main__":
    print("--- Morse Code Encryptor/Decryptor ---")

    # Encryption Example
    message_to_encrypt = input("Enter the message to convert to Morse code: ")
    encrypted = encrypt_to_morse(message_to_encrypt)
    print(f"\nOriginal Text: '{message_to_encrypt}'")
    print(f"Morse Code: '{encrypted}'")

    # Decryption Example
    morse_to_decrypt = input("\nEnter Morse code to decrypt (use space for char sep, ' / ' for word sep): ")
    decrypted = decrypt_from_morse(morse_to_decrypt)
    print(f"Morse Code: '{morse_to_decrypt}'")
    print(f"Decrypted Text: '{decrypted}'")

    print("\n--- Additional Examples ---")
    test_message_1 = "Hello World"
    encrypted_1 = encrypt_to_morse(test_message_1)
    print(f"'{test_message_1}' -> '{encrypted_1}'")
    print(f"'{encrypted_1}' -> '{decrypt_from_morse(encrypted_1)}'")

    test_message_2 = "SOS 123"
    encrypted_2 = encrypt_to_morse(test_message_2)
    print(f"'{test_message_2}' -> '{encrypted_2}'")
    print(f"'{encrypted_2}' -> '{decrypt_from_morse(encrypted_2)}'")

    test_message_3 = "Python is fun!"
    encrypted_3 = encrypt_to_morse(test_message_3)
    print(f"'{test_message_3}' -> '{encrypted_3}'")
    print(f"'{encrypted_3}' -> '{decrypt_from_morse(encrypted_3)}'")