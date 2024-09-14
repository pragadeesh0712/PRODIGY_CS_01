#prodigy infotech cs task 01 - implementation of caeser chiper using python

def caesar_cipher(text, shift, direction):
    shift = shift % 26    
    
    if direction == 'decrypt':
        shift = -shift

    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += new_char
        else:
            encrypted_text += char

    return encrypted_text

def main():
    print("Caesar Cipher Program")
    direction = input("Do you want to encrypt or decrypt? ").lower()
    if direction not in ['encrypt', 'decrypt']:
        print("Invalid option. Please choose 'encrypt' or 'decrypt'.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    result = caesar_cipher(message, shift, direction)
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
