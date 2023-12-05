def create_dict():
    code = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            '0': '-----'}


    reverse = {}
    for entry in code:
        reverse[code[entry]] = entry
    return reverse

def decode_morse(morse_code):
    MORSE_CODE = create_dict()
    output = ''
    for word in morse_code.strip().split('   '):
        for letter in word.split(' '):
            output = output + MORSE_CODE[letter]
        output = output + ' '
    return output.strip()

decode_morse('.... . -.--   .--- ..- -.. .')

def decode_bits(bits):
    index = 0
    output = ''
    while index < len(bits):
        bits.replace('111111', '')
    pass