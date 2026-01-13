def encrypt(char, shift1, shift2):
    if not char.isalpha():
        return char
    if char.islower():
        if 'a' <= char <= 'm':
            shiftVal = (shift1 * shift2) % 13
            return shiftForward('a',shiftVal,char)
        else:
            shiftVal = (shift1 + shift2) % 13
            return shiftBackward('n',shiftVal, char)
    elif char.isupper():
        if 'A' <= char <= 'M':
            shiftVal = shift1 % 13
            return shiftBackward('A',shiftVal,char)
        else:
            shiftVal = (shift2 * shift2) % 13
            return shiftForward('N',shiftVal, char)

def shiftForward(positionFrom, shiftValue, char):
    fwdOffset = ord(char) - ord(positionFrom)
    fwdPosition = (fwdOffset + shiftValue) % 13
    return chr(fwdPosition + ord(positionFrom))
    
def shiftBackward(positionFrom, shiftValue, char):
    bckOffset = ord(char) - ord(positionFrom)
    bckPosition = (bckOffset - shiftValue) % 13
    return chr(bckPosition + ord(positionFrom))
 
def encryptFile(filename, shift1, shift2):
    with open(f"{filename}.txt","r") as file:
        text = file.read()
    result = ""
    for char in text:
        result += encrypt(char,shift1,shift2)
    
    with open("encrypted_text.txt","w") as writeFile:
        writeFile.write(result)