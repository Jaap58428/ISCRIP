# Author:           Jaap Kanbier
# Student number:   s1100592
# Assignment:       Caesar cipher - https://dodona.ugent.be/en/exercises/105361566/

# first input is the amount or the ROT, so 4 means ROT4 encryption
# the secondary input is the actual data that was encoded using this key
# the output is the decrypted value based of the ROT key

if __name__ == '__main__':
    # import both the upper and lowercase alphabetical characters
    from string import ascii_lowercase as lc, ascii_uppercase as uc

    # take user input and convert the ROT key to an integer
    rot_key = int(input("What is the ROT value: "))
    rot_string = input("Which string do you want to decrypt? ")

    # turn the encryption around since we need to translate it back
    rot_key = abs(rot_key - 26)

    # build a translation using slicing based of the key
    rot_table = str.maketrans(lc + uc, lc[rot_key:] + lc[:rot_key] + uc[rot_key:] + uc[:rot_key])

    # display the translation of the string based of the table
    print(rot_string.translate(rot_table))