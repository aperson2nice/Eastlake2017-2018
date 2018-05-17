with open("alphabet", "r") as f:
    letters = f.read().split("\n")
LETTER_HEIGHT = 7 # 7 represents the height of each letter from the file

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

def fancify(name):
    word = ""
    for row_number in range(LETTER_HEIGHT): 
        for letter in name.upper():
            if letter not in alphabet:
                letter = " "
            start = alphabet.index(letter)
            word += letters[start*LETTER_HEIGHT + row_number].strip()
        print(word)
        word = ""

#fancify(input())

def start():
    temp = input("Enter some text (Press Enter twice to End):\n")
    user_input = [temp]
    while True:
        temp = input()
        if temp == "":
            break
        user_input += [temp]

    for words in user_input:
        fancify(words)


if __name__ == __main__:
    start()
