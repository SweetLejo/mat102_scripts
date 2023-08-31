from typing import List
from collections import Counter
import re
import read_file
import matplotlib.pyplot as plt


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


def char_distrobution(message: str):
    most_common: tuple = Counter("".join(re.findall("[a-z]+", message.lower()))).most_common()
    most_common = sorted(most_common, key= lambda x: x[0])
    
    letters = [item[0] for item in most_common]
    occurance = [item[1] for item in most_common]
    plt.bar(letters, occurance)
    plt.xlabel('Letter')
    plt.ylabel('Occurrences')
    plt.title('Letter Occurrences Histogram')
    plt.show()
    


if __name__ == "__main__":
    file = read_file.open_file_and_return_str("romeo_juliet.txt")
    char_distrobution(file)
    
        


    
    