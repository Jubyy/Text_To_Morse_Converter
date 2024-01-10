english_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', ':', '?',
                    '!', '/', '-', '@']
morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----",
                  ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", ".-.-.-", "--..--",
                  "---...", "..--..", "-.-.--", "-..-.", "-....-", "-..-."]


def text_to_morse(input_alphabet: list, morse_output: list):
    final = ''
    print(
        'Write some text in Provided alphabet (Default is English) and this program will give you a Morse code . is '
        'short signal, - is long signal'
        'and space is " / " ')
    word = input('Please give some text: ')
    for one_char in word:
        if one_char == ' ':
            final += ' / '
        else:
            en_char = one_char.upper()
            en_alphabet_index = input_alphabet.index(en_char)
            morse_char = morse_output[en_alphabet_index]
            final += f'{morse_char} '
    print(final)


try:
    text_to_morse(english_alphabet, morse_alphabet)
except ValueError:
    print('\nThere is no characters like this in your alphabet! Try again!!\n')
    try:
        text_to_morse(english_alphabet, morse_alphabet)
    except ValueError:
        print('\nTry again!!\n')

