
def shiftForward(positionFrom, shiftValue, char): # this function contains reusable code to optimize the code length
    """
    Shift a character forward within its 13 half.
    This function encapsulates forward shifting of character to reduce code duplication

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
    This function encapsulates backward shifting of character to reduce code duplication

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
 