def verify():
    with open("raw_text.txt","r") as rawFile:
        rawTxt = rawFile.read()
    with open("decrypted_text.txt","r") as decryptedFile:
        decryptedTxt = decryptedFile.read()
    if(decryptedTxt == rawTxt):
        return "decryption successful!"
    else:   
        return "decryption failed!"