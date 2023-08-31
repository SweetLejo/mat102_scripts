from typing import List
from collections import Counter
import re


def encrypt(string: str, key : int) -> str:
    string = string.lower()
    encrypted : str = ""
    for char in string:
        if char.isalpha():
            encrypted += chr(((ord(char) - 97 + key) % 26) + 97)
        else:
            encrypted += char
    return encrypted


def decrypt(string: str, key : int) -> str:
    return encrypt(string, key * -1)

def dec_list(secret: str) -> List:
    decrypted : List = [];
    for i in range(1, 27):
        decrypted.append(encrypt(secret, i))
    return decrypted

def decrypt_with_e(message: str) -> str: 
    most_common: tuple = Counter("".join(re.findall("[a-z]+", message.lower()))).most_common()
    distance_from_e : int = (ord(most_common[0][0]) - 101) % 26
    return decrypt(message, distance_from_e)


if __name__ == "__main__":
    print(dec_list("uibpmuibqkaqauwzmncvbpivxzwoziuuqvo"))
        


    
    