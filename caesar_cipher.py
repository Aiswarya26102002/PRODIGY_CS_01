def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():

    message = input("Enter the text to encrypt: ")

    while True:
        shift_input = input("enter shift value: ")
        if shift_input.strip().lstrip('-').isdigit():
            shift = int(shift_input)
            break
        else:
            print("❌ Shift must be an integer. Please try again.")

    encrypted = caesar_encrypt(message, shift)
    print(f" Encrypted Message: {encrypted}")

    decrypted = caesar_decrypt(encrypted, shift)
    print(f" Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
