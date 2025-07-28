from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

def sign(filePath=str,privateKeyFile=str):
    with open(privateKeyFile,'r') as p:
        sk = RSA.import_key(p.read())

    with open(filePath,'r') as file:
        content = file.read()

    content = content.encode()
    SHA = SHA256.new(content)
    hashValue = SHA.hexdigest() # Used to return printable hash value
    print("The hash value of this txt file: ", hashValue)
    sign = pkcs1_15.new(sk).sign(SHA)
    print("The signature value of the hashed value: ", sign)
    with open("signature.bin",'wb') as signFile:
        signFile.write(sign)
    
    return sign

def verify(filePath=str,signature=str,publicKeyFile=str):
    with open(publicKeyFile,'r') as p:
        pk = RSA.import_key(p.read())

    with open(filePath,"r") as f:
        content = f.read()

    hashOBJ = SHA256.new(content.encode())

    try:
        pkcs1_15.new(pk).verify(hashOBJ,signature)
        print("signature is valid!")
    except(ValueError,TypeError):
        print("[!] Invalid Signature [!]")


def keyGeneration():
    key = RSA.generate(1024)

    with open("private_key.pem","wb") as private_key:
        private_key.write(key.export_key())

    with open("public_key.pem","wb") as public_key:
        public_key.write(key.public_key().export_key())

def main():
    while True:
        print("[!] Welcome to digital signature generator and verifier [!]")
        print("[1] Generate Keys")
        print("[2] Sign a message")
        print("[3] Verify a message")
        print("[4] Exit")
        cmd = int(input("Enter your choice: "))

        if cmd == 1:
            keyGeneration()
            print("[!] Keys generated successfully [!]")
        elif cmd == 2:
            filePath = input("Enter the file path: ")
            privateKeyFile = input("Enter the private key file path: ")
            signature = sign(filePath=filePath,privateKeyFile=privateKeyFile)
        elif cmd == 3:
            filePath = input("Enter the file path: ")
            publicKeyFile = input("Enter the public key file path: ")
            usingSignFile = input("Do you want to import extneral signature?(Y/n): ")

            if usingSignFile == 'Y':
                signFilePath = input("Enter the signature file path: ")
                with open(signFilePath,'rb') as signFile:
                    signature = signFile.read()

            verify(filePath=filePath,publicKeyFile=publicKeyFile,signature=signature)
        elif cmd == 4:
            print("[!] Goodbye See You Soon [!]")
            exit(0)
        else:
            print("[!] Invalid Choice [!]")
        

if "__main__" == __name__:
    main()
