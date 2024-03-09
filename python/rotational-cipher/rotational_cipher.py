from string import ascii_lowercase

alphabet = ascii_lowercase

def rotate(text, key):
    text_converted = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                text_converted += alphabet[(alphabet.index(letter.lower()) + key) % 26].upper()
            else:
                text_converted += alphabet[(alphabet.index(letter) + key) % 26]
        else:
            text_converted += letter
    return text_converted