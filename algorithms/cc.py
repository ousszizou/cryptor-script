print('''\033[93m
#------------------------------------------------------------------------------#
|                                                                              |
|                                                                              |
|      0000        aa       eeeeeeee   ggggg          aa        oooooooooo     |
|    00           aaaa      ee       gg     gg       aaaa       oo       oo    |
|   00           aa  aa     ee         gg           aa   aa     oo      oo     |
|  00           aa    aa    eeeeeeee     ggg       aa     aa    oooooooo*      |
|   00         aaaaaaaaaa   ee               gg   aaaaaaaaaaa   oo     oo      |
|     00      aa        aa  ee        gg   gg    aa         aa  oo      oo     |
|       0000 aa          aa eeeeeeee    ggg     aa           aa oo       oo    |
|                                                                              |
|                          ======[Caesar Cipher]======                         |
|                                                                              |
|                         \033[97m    Coding By: Algorithm\033[93m                             |
#------------------------------------------------------------------------------#
\033[94m''')

MAX_KEY_SIZE = 26

def getType():
    print('\033[91mwhat is the type of your document?\033[94m')
    type = input().lower()
    if type == 'text':
        mode = getMode()
        message = getMessage()
        if mode[0] != 'b':
            key = getKey()
            print('\033[92mYour translated text is:\033[97m\033[01m')
            print(getTranslatedMessage(mode, message, key))
            print('\033[93mEnd processing! thanks for use our script\033[97m\n')
        else:
            for key in range(1, MAX_KEY_SIZE + 1):
                print(key, getTranslatedMessage('decrypt', message, key))
    elif type == "file":
        fo = input('enter the directory of your file\n')
        try:
            f = open(fo, 'r')
            mode = getMode()
            for l in f:
                if mode in "e encrypt":
                    key = getKey()
                    fo = open('translatedfile.txt', 'a')
                    fo.write(getTranslatedMessage(mode, l, key))
                    msg = "encrypted file succesffuly"
                elif mode in 'd decrypt':
                    key = getKey()
                    fo = open('textfile.txt', 'a')
                    fo.write(getTranslatedMessage(mode, l, key))
                    msg = "decrypted file succesffuly"
                elif mode in 'b brute':
                    fo = open('bruteForceText.txt', 'a')

                    for key in range(1, MAX_KEY_SIZE + 1):
                        fo.write(str(key))
                        fo.write(getTranslatedMessage('decrypt', l, key))
                    msg = "brute force file succesffuly"
            fo.close()
            f.close()
            if msg[0] == 'e':
                print(msg)
                print('\033[93mEnd processing! thanks for use our script\033[97m\n')
            elif msg[0] == 'd':
                print(msg)
                print('\033[93mEnd processing! thanks for use our script\033[97m\n')
            else:
                print(msg)
                print('\033[93mEnd processing! thanks for use our script\033[97m\n')
        except FileNotFoundError:
            print('file not found')
    else:
        print('WOps! you can choose (file) or (text), please choose one of them to continue...')


def getMode():
    while True:
        print('\033[91mDo you want to encrypt or decrypt or brute force a message?\033[94m')
        mode = input().lower()
        if mode in "e encrypt d decrypt b brute":
            return mode[0]
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')

def getMessage():
    print('\033[91mEnter your message text: \033[94m')
    return input()

def getKey():
    key = 0
    print('\033[91mEnter the key number (1-%s)\033[94m' % (MAX_KEY_SIZE))
    key = int(input())
    if (key >= 1 and key <= MAX_KEY_SIZE):
        return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == "d":
        key = -key
    translated = ""

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            if symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

getType()
