alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
    print(char,ord(char),format(ord(char),'b'))

uppercase = alphabet.upper()
for char in uppercase:
    print(char,ord(char),format(ord(char),'b'))