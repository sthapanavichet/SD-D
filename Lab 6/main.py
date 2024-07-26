from cryptography.fernet import Fernet
import base64

def main():
    status = True
    data_key = {}
    while(status):
        method = input("Enter E for Encryption \nEnter D for Decryption\nTo exit the program, enter any other letters\n=>")
        if(method == "E" or method == "e"):
            data = input("Enter a plaintext message: ")
            key = Fernet.generate_key()
            fernet_suite = Fernet(key)
            encrypted_data = fernet_suite.encrypt(data.encode())
            data_key[encrypted_data] = key #storing the key in a dict
            print("Encrypted data in base64: ", base64.b64encode(encrypted_data).decode())


        elif(method == "D" or method == "d"):
            encrypted_data_str = input("Enter the encrypted data: ")
            try:
                encrypted_data = base64.b64decode(encrypted_data_str.encode()) #decoding the base 64 string
            except:
                print("Data entered is invalid or not in the correct format")

            try:
                fernet_suite = Fernet(data_key[encrypted_data])
                decrypted_data = fernet_suite.decrypt(encrypted_data).decode()
                print("Decrypted Data: ", decrypted_data)
            except:
                print("Invalid encrypted data")

        else:
            status = False
        print("\n", end='')

main()