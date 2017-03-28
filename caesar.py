lowerAlpha = "abcdefghijklmnopqrstuvwxyz"
upperAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
    #recieve a letter and returns the 0-based number value for that letter

    dex = lowerAlpha.find(letter)
    if dex < 0:
        dex = upperAlpha.find(letter)

    return dex

def rotate_character(char, rot):
    #recieve a letter and a number and returns a new character based on the number

    position = alphabet_position(char)
    rotated = ''

    if lowerAlpha.find(char) != -1:
        rotated_index = position + rot
        if rotated_index < 26:
            rotated += lowerAlpha[rotated_index]
        else:
            rotated += lowerAlpha[rotated_index % 26]
    elif upperAlpha.find(char) != -1:
        rotated_index = position + rot
        if rotated_index < 26:
            rotated += upperAlpha[rotated_index]
        else:
            rotated += upperAlpha[rotated_index % 26]
    else:
        rotated = char

    return rotated

def encrypt(text, rot):

    encrypted = ''

    for char in text:
        if char == ' ':
            encrypted += char
        else:
            encrypted += rotate_character(char, rot)
    return encrypted
