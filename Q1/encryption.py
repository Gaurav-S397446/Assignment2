def encrypt(char, shift1, shift2):
    if not char.isalpha():
        return char
    if char.islower():
        if 'a' <= char <= 'm':
            offset = ord(char) - ord('a')
            shiftVal = (shift1 * shift2) % 13
            position = (offset + shiftVal) % 13
            return chr(position + ord('a'))
        else:
            offset = ord(char) - ord('n')
            shiftVal = (shift1 + shift2) % 13
            position = (offset - shiftVal) % 13
            return chr(position + ord('n'))
    elif char.isupper():
        if 'A' <= char <= 'M':
            offset = ord(char) - ord('A')
            shiftVal = shift1 % 13
            position = (offset - shiftVal) % 13
            return chr(position + ord('A'))
        else:
            offset = ord(char) - ord('N')
            shiftVal = (shift2 * shift2) % 13
            position = (offset + shiftVal) % 13
            return chr(position + ord('N'))
        
def encryptFile(filename, shift1, shift2):
    with open(f"{filename}.txt","r") as file:
        text = file.read()
    result = ""
    for char in text:
        result += encrypt(char,shift1,shift2)
    
    with open("encrypted_text.txt","w") as writeFile:
        writeFile.write(result)