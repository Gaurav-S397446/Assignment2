def encrypt(char, shift1, shift2):
    
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
     
