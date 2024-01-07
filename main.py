english_alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9','.',',',':','?','!','/','-','@']
morse_alphabet=[".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", ".-.-.-", "--..--", "---...", "..--..", "-.-.--", "-..-.", "-....-", "-..-."]


wynik=''
print('Write some text in English and this program will give you a Morse code . is short signal, - is long signal and space is " / " ')
word=input('Please give some text: ')

for one_char in word:
    if one_char==' ':
        wynik+=' / '
    else:
        en_char=one_char.upper()
        en_alphabet_index=english_alphabet.index(en_char)
        morse_char=morse_alphabet[en_alphabet_index]
        wynik+=f'{morse_char} '
print(wynik)

#s