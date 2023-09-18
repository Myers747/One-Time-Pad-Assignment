import random



def enc():  # Part 1: Encoding Function

    key_file = open("data/key.txt")     # opens and reads the first line into memory for the default key
    sk = key_file.readline()

    plain_file = open("data/plaintext.txt", "r+")       # opens and reads the entirety of plaintext into memory
    m = plain_file.read()

    cipher_file = open("data/ciphertext.txt", "r+")     # opens cipher file to eventually write to it

    bin_m = ''.join(format(ord(i), '08b') for i in m)   # re-formats plaintext into binary

    if len(bin_m) != len(sk):       # raises error if the plaintext binary and the key are not the same length
        raise Exception("error: length is incorrect")

    c = ""

    for i in range(0, len(sk)):     # loop over key length as we add plaintext_binary[1] to key[1]
        c = c + str(int(bin_m[i]) + int(sk[i]))

    cipher_file.write(c)        # write our new cipher to the cipher file

    print("Part 1) encoded cipher: ",c)

    key_file.close()        # close all the files
    plain_file.close()
    cipher_file.close()

    return


def dec():  # Part 2: Decoding Function

    key_file = open("data/key.txt", "r+")       # opens key.txt and takes our key out
    sk = key_file.readline()

    cipher_file = open("data/ciphertext.txt", "r+")     # opens cipher.txt from enc(), and gets cipher text
    c = cipher_file.readline()

    result_file = open("data/result.txt", "r+")     # opens result file for later writing

    if len(sk) != len(c):       # check length of key and cipher to make sure they are the same
        raise Exception("error: length is incorrect")

    bin_m = ""

    for i in range(0, len(sk)):     # subtract the key[i] from the cipher[i]
        bin_m = bin_m + str(int(c[i]) - int(sk[i]))

    m = int(bin_m, 2)       # converts message string to base 2 int
    m = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()       # decodes message to ascii characters

    print("Part 2) decoded cipher message: ",m)

    result_file.write(m)        # write message to result file

    key_file.close()        # close all the files
    cipher_file.close()
    result_file.close()

    return


def keygen():  # Part 3: New Key Generator from input
    new_key_file = open("data/newkey.txt", "r+")        # opens new key for writing our new key later

    new_lambda = int(input("Input an integer from 1 to 128: "))       # takes an int input from the user

    if new_lambda < 1 or new_lambda > 128:      # raises error if new int lambda is < 1 and > 128.
        raise Exception("Error: incorrect input")

    new_key = ""

    while new_lambda > 0:       # appends a random 0 or 1 to the end of our new key while new_lambda > 0
        new_key = new_key + str((random.choice([0, 1])))
        new_lambda = new_lambda - 1     # new_lambda will hit 0, and we will have our new_key at that point

    print("Part 3) new key from input:", new_key)

    new_key_file.write(new_key)     # write new_key to new_key_file

    new_key_file.close()        # close new key file

    return


if __name__ == '__main__':  # main
    enc()
    dec()
    keygen()
