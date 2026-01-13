def encrypt(char, shift1, shift2):
    """
    This function encrypts a character using a a-m and n-z split shift.

    - Following shift rules are applied for each half of the upper and lower case alphabet:
        * Lowercase 'a'-'m': forward shift by (shift1 * shift2)
        * Lowercase 'n'-'z': backward shift by (shift1 + shift2)
        * Uppercase 'A'-'M': backward shift by shift1
        * Uppercase 'N'-'Z': forward shift by (shift2^2)
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

def shiftForward(positionFrom, shiftValue, char): # this function contains reusable code to optimize the code length
    """
    Shift a character forward within its 13 half.

    Parameters:
        positionFrom (str): Starting character of the half alphabet 'a' for 1st half and 'n' for second half
        shiftValue (int): Number of positions to shift forward
        char (str): Character to shift for encryption

    Returns:
        str: Forward shifted or encrypted character
    """
    fwdOffset = ord(char) - ord(positionFrom)
    fwdPosition = (fwdOffset + shiftValue) % 13 # mod 13 round up forward position to half of it's designated alphabets
    return chr(fwdPosition + ord(positionFrom))
    
def shiftBackward(positionFrom, shiftValue, char):  # this function contains reusable code to optimize the code length
    """
    Shift a character backward within its 13 half.

    Parameters:
        positionFrom (str): Starting character of the half alphabet 'a' for 1st half and 'n' for second half
        shiftValue (int): Number of positions to shift backward
        char (str): Character to shift for encryption

    Returns:
        str: Backward shifted or encrypted character
    """
    bckOffset = ord(char) - ord(positionFrom)
    bckPosition = (bckOffset - shiftValue) % 13  # mod 13 round up backward position to half of it's designated alphabets
    return chr(bckPosition + ord(positionFrom))
 
def encryptFile(filename, shift1, shift2):
    """
    this function encrypts the text of a raw_text file and save the encrypted result to 'encrypted_text.txt'.

    Parameters:
        filename (str): Name of the input file (without extension)
        shift1 (int): First shift value
        shift2 (int): Second shift value
    """
    with open(f"{filename}.txt","r") as file:
        text = file.read()
    result = ""
    for char in text:
        result += encrypt(char,shift1,shift2) # encrypt character from file and join as a result
    
    with open("encrypted_text.txt","w") as writeFile:
        writeFile.write(result)