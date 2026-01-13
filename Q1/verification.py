def verify():
    """
    This function verify if original text and decrypted file text matches or not.

    Returns:
        str: Success or Failure message
    """
    with open("raw_text.txt","r") as rawFile:
        rawTxt = rawFile.read() # reads the text of raw_file
    with open("decrypted_text.txt","r") as decryptedFile:
        decryptedTxt = decryptedFile.read() #reads the text of decrypted
    if(decryptedTxt == rawTxt): # checking the content matches or not to find out encryption and decryption are performed correctly
        return "decryption successful!"
    else:   
        return "decryption failed!"