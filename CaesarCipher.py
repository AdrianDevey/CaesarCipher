from cipherArt import logo
def CaesarCipher(plainText, shiftAmount, cipherDirection):
    if direction == "encode":
        cipherText = ""
        for letter in plainText:
            postion = alphabet.index(letter)
            newPosition = postion + shiftAmount

            if newPosition > 26:
                newPosition -= 26
                newLetter = alphabet[newPosition]
            else:
                newLetter = alphabet[newPosition]

            cipherText += newLetter
        print(f'The endoded text is "{cipherText}"')
    elif direction == "decode":
        cipherText = ""
        for letter in plainText:
            postion = alphabet.index(letter)
            newPosition = postion - shiftAmount

            if newPosition < 0:
                newPosition += 26
                newLetter = alphabet[newPosition]
            else:
                newLetter = alphabet[newPosition]

            cipherText += newLetter
        print(f'The decoded text is "{cipherText}"')
    else:
        print("Not a valid choice")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

CaesarCipher(text, shift, direction)