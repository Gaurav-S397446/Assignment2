def decrypt(char, shift1, shift2):
    """
    This function decrypts a character using a-m and n-z split shift.

    - Following shift rules are applied for each half of the upper and lower case alphabet:
    - this function has shifting logic just opposite to encryption due to which decryption will work properly
        * Lowercase 'a'-'m': backward shift by (shift1 * shift2)
        * Lowercase 'n'-'z': forward shift by (shift1 + shift2)
        * Uppercase 'A'-'M': forward shift by shift1
        * Uppercase 'N'-'Z': backward shift by (shift2^2)
    - Non-alphabetic characters or special characters are returned unchanged. 

    Parameters:
        char (str): character to encrypt
        shift1 (int): first shift value
        shift2 (int): second shift value

    Returns:
        str: Encrypted character of char
    """
    if not char.isalpha():
        return char

    if char.islower():
        if 'a' <= char <= 'm':
            offset = ord(char) - ord('a')
            shift_val = (shift1 * shift2) % 13
            position = (offset - shift_val) % 13
            return chr(position + ord('a'))
        elif 'n' <= char <= 'z':
            offset = ord(char) - ord('n')
            shift_val = (shift1 + shift2) % 13
            position = (offset + shift_val) % 13
            return chr(position + ord('n'))
    elif char.isupper():
        if 'A' <= char <= 'M':
            offset = ord(char) - ord('A')
            shift_val = shift1 % 13
            position = (offset + shift_val) % 13
            return chr(position + ord('A'))
        elif 'N' <= char <= 'Z':
            offset = ord(char) - ord('N')
            shift_val = (shift2 ** 2) % 13
            position = (offset - shift_val) % 13
            return chr(position + ord('N'))


def decryptFile(shift1, shift2):
    """
    this function decrypts the text of a encrypted_text file and save the encrypted result to 'decrypted_text.txt'.
    this function separates file read and write from decryption logic and makes code reuseable for different files and shift value

    Parameters:
        shift1 (int): First shift value
        shift2 (int): Second shift value
    """
    with open("encrypted_text.txt","r") as file:
        encryptedTxt = file.read()
    result = ""
    for char in encryptedTxt:
        result += decrypt(char,shift1,shift2)
    with open("decrypted_text.txt","w") as decryptionFile:
        decryptionFile.write(result)