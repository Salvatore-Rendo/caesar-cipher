# The Encryption Function
def cipher_encrypt(plaintext, key):

    encrypted_text = ""

    for char in plaintext:

        if char.isupper(): #check if it's an uppercase character

            char_index = ord(char) - ord('A')

            # shift the current character by key positions
            shifted_char = (char_index + key) % 26 + ord('A')

            new_char = chr(shifted_char)

            encrypted_text = encrypted_text + new_char

        elif char.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            char_index = ord(char) - ord('a') 

            shifted_char = (char_index + key) % 26 + ord('a')

            new_char = chr(shifted_char)

            encrypted_text = encrypted_text + new_char

        elif char.isdigit():

            # if it's a number, just shift 
            new_char = (int(char) + key) % 10

            encrypted_text += str(new_char)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted_text += char

    return encrypted_text

# The Decryption Function
def cipher_decrypt(ciphertext, key):

    decrypted_text = ""

    for char in ciphertext:

        if char.isupper(): 

            char_index = ord(char) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (char_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted_text += c_og

        elif char.islower(): 

            char_index = ord(char) - ord('a') 

            c_og_pos = (char_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted_text += c_og

        elif char.isdigit():

            # if it's a number,shift its actual value 
            c_og = (int(char) - key) % 10

            decrypted_text += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted_text += char

    return decrypted_text

def execute():
    print()
    #list commands
    print("Enter :")
    print("[1] to ENCRYPT a plaintext with the Caesar Cipher")
    print("[2] to DECRYPT a Ciphertext if it was encrypted with the Caesar Cipher")

    #retrivering command
    number = input ( "Enter 1 or 2 : ")

    #Encryption
    if number == "1":

        correct_number= True
        correct_input = False
        while correct_input == False:
            plaintext = input("ENCRYPTION:\nEnter the plaintext that you want to Encrypt: ")
            key = input("Enter the key to Encrypt the text (it must be a number): ")
            if key.isdigit:
                correct_input=True
        ciphertext = cipher_encrypt(plaintext, int(key))
        print(f"Encrypted ciphertext with {key} as a key :", ciphertext)

        #check if you want to continue
        response = input("\nIf you want to continue write [yes] otherwise press Enter to close: ")
        if response.lower() == "yes":
            execute()

    #Decryption
    elif number == "2":
        correct_number= True

        ciphertext = input("DECRYPTION:\nEnter the ciphertext that you want to Decrypt: ")

        #try all keys
        for i in range(26):
            plaintext = cipher_decrypt(ciphertext,i)
            print(f"Plaintext with Key : # {i}: ",plaintext)
        
        #check if you want to continue
        response = input("\nIf you want to continue write [yes] otherwise press Enter to close: ")
        if response.lower() == "yes":
            execute()

    #Bad Command      
    else:  
        print("Wrong input")
        execute()

def main():
    print()
    print("Welcome to the Caesar Cipher CLI software")
    execute()

if __name__ == "__main__":
    main()