from encryption import encryptFile 
from decryption import decryptFile 
from verification import verify 

def main():
    shift1 = int(input("Enter shift1 value:"))
    shift2 = int(input("Enter shift2 value:"))
    encryptFile("raw_text", shift1, shift2)
    decryptFile(shift1, shift2)
    print(verify())

if __name__ == "__main__":
    main()