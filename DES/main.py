#AA1846

from util import DESEncryption,DESDecryption

def main():

    print()
    pText = input("Enter the message to be Eencrypted : ")
    print("\nKey must be 8 length (64-bits) (characters or numbers only)")
    print("\nIf you haven't 8 length key please use -- for rest of space\n Example : -AA1846-\n")
    key = input("Enter Key: ")
    print()

    if len(key) != 8:
        print("Invalid Key. Key should be of 8 length (8 bytes).")
        return

    isPaddingRequired = (len(pText) % 8 != 0)

    ciphertext = DESEncryption(key, pText, isPaddingRequired)

    pText = DESDecryption(key, ciphertext, isPaddingRequired)

    print()
    print("Encrypted Ciphertext is : %r " % ciphertext)
    print("Decrypted pText is  : ", pText)
    print()


if __name__ == '__main__':
    main()