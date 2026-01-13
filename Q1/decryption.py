def decrypt(char, shift1, shift2):
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
    with open("encrypted_text.txt","r") as file:
        encryptedTxt = file.read()
    result = ""
    for char in encryptedTxt:
        result += decrypt(char,shift1,shift2)
    with open("decrypted_text.txt","w") as decryptionFile:
        decryptionFile.write(result)