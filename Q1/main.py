from encryption import encryptFile 
from decryption import decryptFile 
from verification import verify 

def main():
    """
    This function performs file encryption, decryption, and verification.

    --------------------------
    - Handles user input for dynamic shift values.
    - Calls encrypt and decrypt function from external package.
    - Verifies that if decryption has restored to the original file content.
    - It includes error handling to ensure only valid datatype are used for shifts.
    """
    while True:
        try:
            shift1 = int(input("Enter shift1 value:"))
            shift2 = int(input("Enter shift2 value:"))
            encryptFile("raw_text", shift1, shift2)
            decryptFile(shift1, shift2)
            print(verify())
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()