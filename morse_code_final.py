# Define the Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def morse_to_text(morse_code):
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
        '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
        '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
        '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '/': ' ', '': ''  # Adding mapping for space
    }

    morse_words = morse_code.split('  ')
    text = ''

    for morse_word in morse_words:
        morse_letters = morse_word.split(' ')
        for morse_letter in morse_letters:
            if morse_letter in morse_code_dict:
                text += morse_code_dict[morse_letter]
        text += ' '

    return text.strip()

def morse_to_binary(morse_code):
    charactersList = list(morse_code)
    n = len(charactersList)
    i =0
    binary_code =''
    while i<n-1:
        if charactersList[i] == '.':
            binary_code += '1'
            if n-i==1:
                binary_code += ''
            elif charactersList[i+1] != ' ':
                binary_code += '0'
        elif charactersList[i] == '-':
            binary_code += '111'
            if n-i==1:
                binary_code += ''
            elif charactersList[i+1] != ' ':
                binary_code += '0'
        elif charactersList[i] == ' ':
            if charactersList[i-1] == ' ':
                binary_code += '0000'
            else:
                binary_code +='000'
        i+=1
    return(binary_code)

def text_to_morse(text):
    text.lstrip()
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code += ' '
    return morse_code

def binary_to_morse(binary_code):
    binary_list = list(binary_code)
    n = len(binary_list)
    i = 0
    morse_code = ''
    oneCount =0
    zeroCount =0
    while i < n-1:
        while binary_list[i] != '1':
            i+=1
            zeroCount +=1
        if zeroCount ==3:
            morse_code += ' '
        elif zeroCount ==7:
            morse_code += '  '
        zeroCount = 0
        if n-i != 1:
            if n-i ==3:
                if binary_list[i+1] =='0':
                    morse_code += '..'
                    i+=3
                else:
                    morse_code += '-'
                    i+=3
            else:
                while binary_list[i] == '1':
                    i+=1
                    oneCount +=1
                if oneCount ==1:
                    morse_code += '.'
                elif oneCount ==3:
                    morse_code += '-'
                oneCount = 0
        elif n-i == 1:
            morse_code += '.'
            i+=1
    return morse_code

user_input = input("Enter text to translate to Morse code: ")

# Translate and print the Morse code
morse_result = text_to_morse(user_input)
print("Morse code:", morse_result)


binary_result = morse_to_binary(morse_result)
print("Binary representation:", binary_result)

morse_output = binary_to_morse(binary_result)
text_output = morse_to_text(morse_output)

print("Morse code:", morse_output)
print("Text:", text_output)
