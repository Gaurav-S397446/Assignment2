from shiftPosition import shiftBackward, shiftForward

def decrypt(char, shift1, shift2):
    if not char.isalpha():
        return char

    if char.islower():
        if 'a' <= char <= 'm':
            shiftVal = (shift1 * shift2) % 13
            return shiftBackward('a',shiftVal, char)
        elif 'n' <= char <= 'z':
            shiftVal = (shift1 + shift2) % 13
            return shiftForward('n',shiftVal, char)
    elif char.isupper():
        if 'A' <= char <= 'M':
            shiftVal = shift1 % 13
            return shiftForward('A',shiftVal, char)
        elif 'N' <= char <= 'Z':
            shiftVal = (shift2 ** 2) % 13
            return shiftBackward('N',shiftVal, char)

def decryptFile(shift1, shift2):
    with open("encrypted_text.txt","r") as file:
        encryptedTxt = file.read()
    result = ""
    for char in encryptedTxt:
        result += decrypt(char,shift1,shift2)
    with open("decrypted_text.txt","w") as decryptionFile:
        decryptionFile.write(result)